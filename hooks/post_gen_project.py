import subprocess

remoteOrigin = "{{cookiecutter.remoteOrigin}}"

#Initialize git
subprocess.run("git init")

#Add all content
subprocess.run("git add .")

#Make first commit
subprocess.run("git commit -a -m \"first commit: python package template from https://github.com/PaoloGinefra/PythonPackageCookieCutterTamplate\"")

if remoteOrigin != "None":
    #Add remote origin
    subprocess.run(f"git remote add origin {remoteOrigin}")

    #Ensures main branch
    subprocess.run("git branch -M main")

    #Push to the gh repo
    subprocess.run("git push -u origin main")
