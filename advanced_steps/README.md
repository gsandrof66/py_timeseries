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

bazel build //tensorflow/tools/pip_package:wheel --repo_env=WHEEL_NAME=tensorflow_cpu --local_ram_resources=2048 --config=monolithic --verbose_failures -c opt --config=opt --copt=-Wno-gnu-offsetof-extensions --copt=-march=native --copt=-mavx --copt=-mavx2 --copt=-mfma --copt=-msse4.1 --copt=-msse4.2
