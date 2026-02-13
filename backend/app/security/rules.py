SECURITY_PATTERNS = {
    "hardcoded_secret": ["password=", "api_key=", "secret="],
    "sql_injection": ["execute(", "cursor.execute", "SELECT * FROM"],
    "command_injection": ["os.system", "subprocess.Popen"],
    "insecure_http": ["http://"]
}
