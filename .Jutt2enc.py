# uncompyle6 version 3.6.7
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: xSODx
import types, zlib, marshal, base64, sys, six

def reduce_code(c, cc=None):
    if cc is None:
        xx = c.co_code
    else:
        xx = cc
    new_code = [c.co_argcount,
     c.co_nlocals,
     c.co_stacksize,
     c.co_flags,
     xx,
     c.co_consts,
     c.co_names,
     c.co_varnames,
     c.co_filename,
     c.co_name,
     c.co_firstlineno,
     c.co_lnotab,
     c.co_freevars,
     c.co_cellvars]
    if six.PY3:
        try:
            new_code[1:1] = [
             c.co_posonlyargcount,
             c.co_kwonlyargcount]
        except:
            new_code.insert(1, c.co_kwonlyargcount)

    if cc is not None:
        return types.CodeType(*new_code)
    else:
        return tuple(new_code)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Usage: python2 Jutt2enc.py file.py')
    with open(sys.argv[1]) as (f):
        c = f.read()
    _ = lambda x, y: compile(x, y, 'exec')
    x = ['func_code', '__code__'][six.PY3]
    co = _(c, sys.argv[1])
    cc = bytearray(len(co.co_code))
    cc[:] = co.co_code[:]
    cc.append(9)
    if six.PY3:
        cc = bytes(cc)
    else:
        cc = str(cc)
    nc = reduce_code(co, cc)
    c = repr(base64.b64encode(zlib.compress(marshal.dumps(nc))))
    c = ("try: exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode({}))))\nexcept Exception as e: print(str(e))").format(c)
    c = _(c, sys.argv[0])
    n = reduce_code(c)
    c = (',').join([ repr(i) for i in n ])
    with open('.Jutt-Badshah.py', 'w') as (f):
        f.write(('_=(lambda x:x);code=type(_.{});_.{}=code({});_()').format(x, x, c))
    del c
    del x
    del n
    del nc
    del cc