#### matchObj.groups(), matchOb.lastGroupName 和 matchObj.group(group1[,group2,...]) 使用
```python                                                              
# 当使用分组时 match 为一个元组 此时用 groups() 获取该元组 用group() 获取单个或多个指定的元组
# 当未使用分组时 match 为一个字符串 可以使用 group() 直接获取该匹配                          
pattern = re.compile(r'(\d)(\d)(\d)(?P<lastGroupName>\d)')                                   
	match = pattern.match('1982')                                                                
print(match.groups())                                                                        
	print(match.group(1, 3))  # 若结果为元组时 元组的第一个元素为被操作的字符串                  
	print(match.lastgroup)  # 获取最后一个组的组名                                               

	```

### matchObj.groupdict() 使用  
	```python                                                          
	match = re.match(r'(?P<firstName>\w+) (?P<lastName>\w+)', 'zhaoyingnan zhaoyn')
	print(match.groupdict())  # {'lastName': 'zhaoyn', 'firstName': 'zhaoyingnan'}
	```

### matchObj.search(string[, startpos[, endpos]]) 使用
	```python
# startpos 和 endpos 代表从 string 的 startpos 索引开始匹配 到 endpos 结束 索引从0开始
	pattern = re.compile(r'dog', re.I)  # 创建一个pattern对象
	match = pattern.search('adogs', 1, 4)  # 从 adogs 的索引为1的位置开始匹配 到索引位置为4时结束匹配
	print(match.group(0))  # dog      
	print(match.start())  # 1 返回开始位置的索引值     
	print(match.end())  # 4 返回结束位置的索引值            
	print(match.span())  # (1, 4) 返回开始和结束位置的索引值的元组
	```

### matchObj.sub(pattern, replace or function, str, count=0, flags=0) 使用
	```python
# sub(pattern, replace or function, str, count=0, flags=0) 字符串替换 返回替换后的字符串
	str1 = 'Baked Beans And Spam'                 
	print(re.sub(r'\sand\s', ' & ', str1, flags=re.I))  # Baked Beans & Spam                                                                                     
	print(re.sub(r'\d+', add, '1 2 3'))  # 2 4 6
	```

