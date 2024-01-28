USER="admin"
PASS="super_password"
MAIL="admin@mail.com"
NAME="Admin"
script="
from user.models import User;

username = '$USER';
password = '$PASS';
email = '$MAIL';
fullName = '$NAME';

if User.objects.filter(username=username).count()==0:
    User.objects.create_superuser(email, username, fullName, password);
    print('Superuser created.');
else:
    print('Superuser creation skipped.');
"
printf "$script" | python manage.py shell