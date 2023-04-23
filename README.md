
<!-- TOC -->

- [Python后端开发知识梳理](#python后端开发知识梳理)
    - [python 2/3的区别](#python-23的区别)
        - [Python3的优化](#python3的优化)
        - [Python3 新增](#python3-新增)
        - [Python3 改进](#python3-改进)
        - [Python 2/3工具](#python-23工具)
    - [Python 函数](#python-函数)
    - [Python 异常机制](#python-异常机制)
    - [Python 性能分析与优化， GIL 常考题](#python-性能分析与优化-gil-常考题)
        - [什么是CPython GIL？](#什么是cpython-gil)
        - [GIL的影响](#gil的影响)
        - [如何规避GIL](#如何规避gil)
        - [GIL的实现](#gil的实现)
        - [为什么有了GIL线程安全还要关注线程安全](#为什么有了gil线程安全还要关注线程安全)
        - [剖析程序性能](#剖析程序性能)
        - [服务端性能优化](#服务端性能优化)
    - [Python生成器与协程](#python生成器与协程)

<!-- /TOC -->
# Python后端开发知识梳理

1. Python 是一个动态强类型语言 （没有类型隐式转换）

```bash
>>> 1 + '1'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

2. python2/3 不兼容

3. 什么是自省？

运行时判断一个对象的类型的能力

Python一切皆对象，用type,id,instance获取对象类型信息

4. monkey patch 运行时属性替换

5. is 判断对象

6. 列表推导式

```bash
# 字典推导式
{k:v for k, v in zip(a,b)}

# list
[i for i in range(10)]

# set
(i for i in range(10)) 
返回类型为generator
```

7. 鸭子类型duck typing

[https://zh.wikipedia.org/wiki/鸭子类型](https://zh.wikipedia.org/wiki/%E9%B8%AD%E5%AD%90%E7%B1%BB%E5%9E%8B)

当看到一个鸟走起来像鸭子、游泳起来像鸭子、叫起来像鸭子、那么这只鸟就可以被称为鸭子。

在鸭子类型中，关注点在于对象的行为，能做什么。 关注的是方法、属性。不关注对象

## python 2/3的区别

### Python3的优化

1. print 成为函数
2. 编码问题 python3 不在有unicode对象，默认str就是unicode     
3. 除法变化。python3 除号返回浮点数  整除使用 "//"
4. 类型注解（type hint)。 帮助ide实现类型检查  通过第三方工具mypy 进行类型检查

    ```python
    def hello(name: str) -> str:
        return 'hello' + name
    ```

5. 优化super() 方便直接调用父类函数
6. 高级的解包操作。 a, b, *rest = range(10)
7. 限定关键字参数
8. python3 重新抛出异常不会丢失栈信息  raise  xxxError from xxxError
9.  一切返回迭代器 range, zip, map, dict, values, etc. all iterators

### Python3 新增

1. yield from 链接子生成器
2. asyncio 内置库， async/await 原生协程支持异步编程
3. 新的内置库 enum（枚举）, mock（单元测试 ）, asynico, ipaddress, concurrent.futures 等

### Python3 改进

生成的pyc文件统一放到`__pycache__`

一些内置库的修改  `urllib,selector`等

性能的优化等

### Python 2/3工具

`six`模块

`2to3` 等工具转换代码

`__future__`

## Python 函数

1. 参数传递
2. 可变对象    `list  dict  set`   
3. 不可变对象   `str  bool int float tuple frozenset`     类似传值
4. 可变类型作为参数

    Python 使用对象引用

    Python如何来传递参数？

    唯一支持的参数传递是共享传参  call by object (call by object reference or call by sharing)  

    call by sharing 函数形参获得实参中各个引用的副本

    可变参数做为默认参数   默认参数只计算一次

5. 不可变类型作为参数
6. Python *args, **kwargs 含义

    用来处理可变参数

    *args 被打包成tuple

    **kwargs 被打包成dict

## Python 异常机制

BaseException

SystemExit      系统退出

KeyboardInterrupt  关键字异常

GeneratorExit

Exception

1. 什么时候需要捕获异常？ 
    1.  网络请求超时、连接错误等
    2. 资源访问， 权限问题， 资源不存在
    3. 代码逻辑 越界访问、KeyError

    ```bash
    try:
    		func()
    except Exception1 as e:
        # 异常处理的代码
    else:
    		# 异常没有发生的时候代码逻辑
        pass
    finally:
    		# 无论异常有没有发生都会执行的代码，一般处理资源的关闭和释放
    		pass

    ```

2. 如何自定义异常？
    1. 继承`Exception`实现自定义异常
    2. 给代码附加一些信息
    3. 处理业务相关的特定的异常 `raise MyException`

## Python 性能分析与优化， GIL 常考题

### 什么是CPython GIL？

> In CPython, the global interpreter lock, or GIL, is a mutex that prevents multiple native threads from executing Python bytecodes at once. This lock is necessary mainly because CPython’s memory management is not thread-safe. (However, since the GIL exists, other features have grown to depend on the guarantees that it enforces.)

> 在 CPython 中，全局解释器锁或 GIL 是一个互斥锁，可防止多个本地线程同时执行 Python 字节码。 这个锁是必要的，主要是因为 CPython 的内存管理不是线程安全的。 （但是，由于 GIL 存在，其他功能已经发展到依赖于它强制执行的保证。）

GIL Global Interpreter Lock

Cpython 解析器的内存管理并不是线程安全的

保护多线程情况下对Python对象的访问

Cpython 使用简单的锁机制避免多个线程同时执行字节码（Python 是通过讲Python文件编写成字节码来执行的）

### GIL的影响

限制了程序的多核执行

同一个时间只能有一个线程执行字节码

CPU密集程序难以利用多核优势

IO期间会释放GIL, 对IO密集程序印象不大

### 如何规避GIL

区分程序是CPU密集型还是IO密集型

CPU密集可以使用多进程+进程池

IO密集型使用多线程、协程

`cython`扩展

### GIL的实现

在一定时间内`ticks`，重新释放锁。让其他的线程运行

### 为什么有了GIL线程安全还要关注线程安全

Python中什么操作才是原子的？ 一步到位执行完

一个操作如果是一个字节码指令可以完成就是原子的

原子的是可以保证线程安全的

使用dis操作来分析字节码

 

### 剖析程序性能

使用各种profile工具 内置或者第三方

二八定律，大部分时间耗费在少量代码上

内置的profile/cprofile等工具

使用`pyflame`(uber开源)的火焰图工具

### 服务端性能优化

web应用一般语言不会成为瓶颈

数据结构与算法优化

数据库层：添加索引优化，慢查询消除，批量操作减小IO，NoSQL

网络IO: 批量操作， `pipline`操作 减少IO

缓存：使用内存数据库 `redis`/`memcache`

异步： `asyncio`, `celery`

并发：gevent/多线程

## Python生成器与协程

1. 生成器 `generator`

    生成器就是可以生产值的函数

    当一个函数有了 yield 关键字就成了生成器

    生成器可以挂起执行并且保持当前执行的状态

2. 基于生成器的协程

    Python3之前没有原生协程，只有基于生成器的协程

    pep342 增强生成器功能

    生成器可以通过yield暂停执行和产出数据

    同时支持send()向生成器发送数据和throw()向生成器抛出异常

3. 协程注意点

    协程需要使用send(None)或者next(coroutine)来预激prime才能启动

    在yield处协程会暂停执行

    单独的yield value 会产出值给调用方

    可以通过coroutine.send(vlaue)来给协程发送值，发送的值会赋值给yield表达式左边的变量 value= yield

    协程执行完成后（没有遇到下一个yield语句）会抛出StopIteration异常

    协程装饰器

    ```python
    from functiools import wraps
    def coroutine(func):
        @wraps(func)
        def primer(*args, **kwargs):
            gen = func(*args, **kwargs)
            next(gen)
            return gen
        return primer
    ```

    python3 原生线程

    python3.5 引入async/await 支持原生协程native coroutine