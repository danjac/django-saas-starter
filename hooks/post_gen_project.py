import secrets
import string

ALLOWED_CHARS = string.ascii_letters + string.digits


def get_random_string(length=50):
    return "".join(secrets.choice(ALLOWED_CHARS) for i in range(length))


def generate_env_file():
    secret_key = get_random_string()
    with open(".env", "w") as fp:
        fp.write(f'SECRET_KEY="{secret_key}"\n')

        for aws_key in (
            "AWS_ACCESS_KEY_ID",
            "AWS_SECRET_ACCESS_KEY",
            "AWS_STORAGE_BUCKET_NAME",
        ):
            fp.write(f'{aws_key}="****"\n')


def main():
    generate_env_file()


if __name__ == "__main__":
    main()
