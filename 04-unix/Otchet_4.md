### Отчёт по заданию 4

- Изначально была выполнена команда: `docker run -it --rm ubuntu:22.04 bash`

- Успешно выполнено `apt-get update`, часть вывода представлена ниже:
Hit1 httparchive.ubuntu.comubuntu noble InRelease
Hit2 httparchive.ubuntu.comubuntu noble-updates InRelease
Hit3 httparchive.ubuntu.comubuntu noble-backports InRelease
Hit4 httpsecurity.ubuntu.comubuntu noble-security InRelease
Reading package lists...

Вывод подтвердил доступ к интернету. Попытки использовать `iptables` и `ip route` не удались из-за отсутствия привилегий, что связано с ограничениями Docker без изменения флагов.


- Для блокировки к интернету был очищен `/etc/resolv.conf` командой `echo "" > /etc/resolv.conf` (удалены DNS-серверы). `apt-get update` вернул ошибки, представленные ниже:
Ign:1 http://archive.ubuntu.com/ubuntu noble InRelease
Ign:2 http://archive.ubuntu.com/ubuntu noble-updates InRelease
Ign:3 http://archive.ubuntu.com/ubuntu noble-backports InRelease
....
Err:1 http://archive.ubuntu.com/ubuntu noble InRelease
  Temporary failure resolving 'archive.ubuntu.com'
Err:2 http://archive.ubuntu.com/ubuntu noble-updates InRelease
  Temporary failure resolving 'archive.ubuntu.com'
....


- В качестве дополнительного способа были добавлены записи в `/etc/hosts` командами `echo "127.0.0.1 archive.ubuntu.com" >> /etc/hosts` и `echo "127.0.0.1 security.ubuntu.com" >> /etc/hosts`, после чего `apt-get update` вернул ошибки, подтверждая блокировку. 