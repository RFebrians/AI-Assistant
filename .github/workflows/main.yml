name: Build
on:
  push:

jobs:
# Build job. Builds app for Android with Buildozer
build-android:
  name: Build for Android
  runs-on: ubuntu-latest

  steps:
    - name: Checkout
      uses: actions/checkout@v2

    - name: Build with Buildozer
      uses: ArtemSBulgakov/buildozer-action@v1
      id: buildozer
      with:
        workdir: <specify the directory of the app no don't mention this the app files are in root directory>
        buildozer_version: stable

    - name: Upload artifacts
      uses: actions/upload-artifact@v2
      with:
        name: package
        path: ${{ steps.buildozer.outputs.filename }}
