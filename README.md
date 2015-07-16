Change iTerm background color [red, green, blue := 0~255]

```sh
% chtermbg $red $green $blue
```


Save current environment python-virtualenv for calling when terminal runs

```sh
% reservework
```


Input filename then output filename zero-padded
```sh
% zeropad xxx1.zip  # -> xxx00001.zip
% ls *.jpg | xargs -n 1 zeropad
```


Output command used on python-shell to file (default filename is 'history.py')
Need to make a path
```python
>>> for x in (1,2):
...  print(x)
...
1
2
>>> wh()  # OR wh('history.py')
>>>
```
```sh
% cat history.py
for x in (1,2):
 print(x)
```
