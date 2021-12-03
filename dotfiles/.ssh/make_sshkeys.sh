#!/bin/bash

# key for github
ssh-keygen -f id_rsa_github -t rsa -N ""

# key for systemC (sekirei)
ssh-keygen -f id_rsa_buseiC -t rsa -N ""


# key for systemB (ohtaka)
ssh-keygen -f id_rsa_ohtaka2 -t rsa -N ""


# key for systemC new (enaga)
ssh-keygen -f id_rsa_buseiC2 -t rsa -N ""

