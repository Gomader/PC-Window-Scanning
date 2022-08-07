# PC-Window-Scanning

- python 3.7.6
- PyQt5 5.15.4
- opencv 4.5.1.48

# 问题
- 此代码只能匹配相同清晰度、shape的图片，如果分辨率不一样，可能要调整一下threshold，目前设定为0.6，测试降低之后分辨率不同的图片可以匹配到，但是错误率很高