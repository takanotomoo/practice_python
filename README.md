【Django】
★サーバーを起動させる。
python manage.py runserver


★DBの更新反映
①python manage.py makemigration
② python manage.py migrate





※スーパーユーザーの作成
python manage.py createsuperuser


【gitへの上げ方】
cd \Anali\py\djangosnippets\djangosnippets
git add --all
git commit -m "更新"
git push origin master
