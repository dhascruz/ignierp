from passlib.hash import phpass, bcrypt, sha512_crypt, md5_crypt


def check_moodle_password(password, hash_from_db):
    """
    Verify Moodle password against multiple possible hash types.
    """
    if hash_from_db.startswith('$2y$') or hash_from_db.startswith('$2a$'):
        # bcrypt
        return bcrypt.verify(password, hash_from_db)
    elif hash_from_db.startswith('$P$'):
        # phpass (Moodle default)
        return phpass.verify(password, hash_from_db)
    elif hash_from_db.startswith('$6$'):
        # sha512 crypt
        return sha512_crypt.verify(password, hash_from_db)
    elif hash_from_db.startswith('$1$'):
        # md5 crypt
        return md5_crypt.verify(password, hash_from_db)
    else:
        raise ValueError(f"Unknown hash format: {hash_from_db}")
    


