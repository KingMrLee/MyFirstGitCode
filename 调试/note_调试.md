# 调试技术
- 调试流程：单元测试->集成测试->交测试部
- 分类：
    - 静态调试；单纯地看代码查bug    
    - 动态调试；程序跑起来调试代码
## pdb调试
- 之前的调试方法：pdb调试，命令行调试
# pycharm调试
- run/debug模式
- 案例01.py        
    - 断点：程序的某一行，在debug模式下，遇到断点就自动暂停
        - 先debug模式运行代码，然后打断点，再debug模式运行程序，会跳转到Debugger下，stepover(F8)：
        把后面的程序都执行完；step into(F7)：进入到当前这一步，逐行执行；建议先F8看当前函数的结果对不对，然后
        再F7进入函数体查看是否有问题；
         
# 单元测试
