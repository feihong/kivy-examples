# Kivy Examples

## Installation

### Ubuntu

To install Kivy on Ubuntu 14.04, refer to the following script: https://github.com/brousch/kivy-installer/blob/master/ubuntu/1404/python27/kivy_all.sh

There's no need to go through the PPA as per the official installation instructions.

### Mac

[Download the .7z file for Python 3](https://kivy.org/#download) and install `Kivy3.app` to your Applications folder.

Make a symbolic link so that you have access to the `kivy` command:

```
ln -s /Applications/Kivy3.app/Contents/Resources/script /usr/local/bin/kivy
```

## Building and running on Android

To build mobile programs for your Android device, run this:

```
buildozer -v android debug
```

Transfer the resulting .apk file to your device. I usually just drag it into a Dropbox folder and open it from my phone.

## Sources

[Installation on OS X](https://kivy.org/docs/installation/installation-osx.html)
