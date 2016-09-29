#!/usr/bin/python
# -*- coding: UTF-8 -*-
for num in range(100,200 + 1):
	# 素数大于 1
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				break
		else:
			print(num)
