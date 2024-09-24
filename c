[1mdiff --git a/.github/workflows/pre-commit.yml b/.github/workflows/pre-commit.yml[m
[1mindex c7f38c9..9f6d4b3 100644[m
[1m--- a/.github/workflows/pre-commit.yml[m
[1m+++ b/.github/workflows/pre-commit.yml[m
[36m@@ -11,4 +11,4 @@[m [mjobs:[m
     steps:[m
     - uses: actions/checkout@v3[m
     - uses: actions/setup-python@v3[m
[31m-    - uses: pre-commit/action@v3.0.1[m
\ No newline at end of file[m
[32m+[m[32m    - uses: pre-commit/action@v3.0.1[m
[1mdiff --git a/.pre-commit-config.yaml b/.pre-commit-config.yaml[m
[1mindex fa41c51..b7a7cdc 100644[m
[1m--- a/.pre-commit-config.yaml[m
[1m+++ b/.pre-commit-config.yaml[m
[36m@@ -9,4 +9,3 @@[m [mrepos:[m
     rev: 22.10.0[m
     hooks:[m
     -   id: black[m
[31m-[m
[1mdiff --git a/README.md b/README.md[m
[1mindex c140f99..dbe3548 100644[m
[1m--- a/README.md[m
[1m+++ b/README.md[m
[36m@@ -1,5 +1,5 @@[m
 # repSoftTestClass[m
[31m-This repository is for the Software Testing Class 2024. [m
[32m+[m[32mThis repository is for the Software Testing Class 2024.[m
 [m
 [m
 # Specification[m
