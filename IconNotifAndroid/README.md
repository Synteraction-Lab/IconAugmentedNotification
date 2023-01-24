# IconNotifAndroid
A branch of [HeadsUpGlass](https://github.com/NUS-HCILab/HeadsUpGlass) (and private repo [NIPGlass](https://github.com/NUS-HCILab/NIPGlass)) which display custom content on Android based OHMD (e.g., Vuzix Blade, Epson BT-300)


## Requirements
1. AndroidStudio (or any IDE which support Android)
2. Android SDK (AndroidStudio will directly download this for you)


## How to run?
1. Build the project first (Make Tool)
2. Run the app
3. If you get error saying that `credential` file missing, add an empty json file (i.e. `credential.json` with content `{}`) to `res/raw/`
4. See more details at [HeadsUpGlass](https://github.com/NUS-HCILab/HeadsUpGlass) 


### Python app
- install the corresponding Python app in [IconNotifPython](../IconNotifPython) on a computer to trigger the notifications


### References
- Git model: https://nvie.com/posts/a-successful-git-branching-model/
- Android: https://developer.android.com/guide/components/fundamentals?hl=en, https://developer.android.com/courses/fundamentals-training/overview-v2
- Android architecture: https://developer.android.com/jetpack/docs/guide 
- Android context: https://blog.mindorks.com/understanding-context-in-android-application-330913e32514 
- Dagger: https://google.github.io/dagger/android.html, https://guides.codepath.com/android/dependency-injection-with-dagger-2
- RESTful API: https://github.com/NationalBankBelgium/REST-API-Design-Guide/wiki,  https://github.com/Microsoft/api-guidelines


