import subprocess
from .models import CourseBackup

def run_course_backup(course_id, destination):
    backup = CourseBackup.objects.create(
        course_id=course_id,
        file_path=f"{destination}/course_{course_id}.mbz",  # Moodle default extension
        status="pending"
    )

    try:
        # Command to run Moodle backup
        command = [
            "php", "/var/www/html/igni/admin/cli/backup.php",
            f"--courseid={course_id}",
            f"--destination={destination}"
        ]

        result = subprocess.run(command, capture_output=True, text=True, check=True)

        # Update status if successful
        backup.status = "success"
        backup.save()

        return result.stdout

    except subprocess.CalledProcessError as e:
        backup.status = "failed"
        backup.file_path = ""
        backup.save()
        return f"Error: {e.stderr}"    