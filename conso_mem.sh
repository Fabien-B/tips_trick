#!/bin/bash
ps -eo pmem,pid | sort -r | grep $1
