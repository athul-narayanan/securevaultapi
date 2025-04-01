openssl rsa -in certs/django_local.key -passin pass:"Algoma@2024" -out certs/localhost_decrypted.key

daphne -e ssl:8000:privateKey=certs/localhost_decrypted.key:certKey=certs/django_local.crt securevaultapi.asgi:application

shred -u certs/localhost_decrypted.key