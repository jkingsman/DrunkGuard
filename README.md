DrunkGuard
==========

Plugin for the yum package manager that will force you to do math problems to prove sobriety before using it.


Installation
==========

Ensure you have plugins enabled in your yum config (`/etc/yum.conf`):

`plugins=1`

Then download the configuration and plugin files from GitHub:

```
wget https://raw.githubusercontent.com/jkingsman/DrunkGuard/master/drunkguard.conf
wget https://raw.githubusercontent.com/jkingsman/DrunkGuard/master/drunkguard.py
```

Move the files into place:

```
sudo mv drunkguard.conf /etc/yum/pluginconf.d/drunkguard.conf
sudo mv drunkguard.py /usr/lib/yum-plugins/drunkguard.py
```

You can customize your desired days and hours for drunk checking in `drunkguard.py`. The default is 8PM to 6AM, Friday, Saturday, and Sunday.

You're now good to go!

```
[jkingsman@eruditorum ~]$ yum remove git
Loaded plugins: drunkguard, fastestmirror
Hm... are you drunk?
What is 18 + 28? 46
Well done!
What is 100 + 94? 194
Well done!
What is 45 + 49? 93

That's not right... You're drunk! No yum for you.

```
