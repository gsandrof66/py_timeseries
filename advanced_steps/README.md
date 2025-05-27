# Customised tensorflow
In order to solve this warning "rebuild TensorFlow with the appropriate compiler flags for AVX2 FMA"
You will need bazel

Run:
./configure
When prompted:
Python location: enter your Python 3 path (e.g., /usr/bin/python3)
CUDA/ROCm: answer according to your setup (probably "No" if you’re CPU-only)
**Clang you need it)
Optimization flags: here's the key part!

You need to run this command:
bazel build --config=opt \
  --copt=-march=native \
  --copt=-Wno-sign-compare \
  --copt=-Wno-unused-result \
  //tensorflow/tools/pip_package:build_pip_package
