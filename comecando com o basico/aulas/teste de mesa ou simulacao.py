Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print (´alo´)
SyntaxError: invalid character in identifier
>>> 3+2
5
>>> print ('alo')
alo
>>> 5-4
1
>>> 4*8
32
>>> 7/8
0.875
>>> type 8
SyntaxError: invalid syntax
>>> type (8)
<class 'int'>
>>> type (3.149)
<class 'float'>
>>> type ('oi')
<class 'str'>
>>> 
2**10
1024
>>> 2**10000
19950631168807583848837421626835850838234968318861924548520089498529438830221946631919961684036194597899331129423209124271556491349413781117593785932096323957855730046793794526765246551266059895520550086918193311542508608460618104685509074866089624888090489894838009253941633257850621568309473902556912388065225096643874441046759871626985453222868538161694315775629640762836880760732228535091641476183956381458969463899410840960536267821064621427333394036525565649530603142680234969400335934316651459297773279665775606172582031407994198179607378245683762280037302885487251900834464581454650557929601414833921615734588139257095379769119277800826957735674444123062018757836325502728323789270710373802866393031428133241401624195671690574061419654342324638801248856147305207431992259611796250130992860241708340807605932320161268492288496255841312844061536738951487114256315111089745514203313820202931640957596464756010405845841566072044962867016515061920631004186422275908670900574606417856951911456055068251250406007519842261898059237118054444788072906395242548339221982707404473162376760846613033778706039803413197133493654622700563169937455508241780972810983291314403571877524768509857276937926433221599399876886660808368837838027643282775172273657572744784112294389733810861607423253291974813120197604178281965697475898164531258434135959862784130128185406283476649088690521047580882615823961985770122407044330583075869039319604603404973156583208672105913300903752823415539745394397715257455290510212310947321610753474825740775273986348298498340756937955646638621874569499279016572103701364433135817214311791398222983845847334440270964182851005072927748364550578634501100852987812389473928699540834346158807043959118985815145779177143619698728131459483783202081474982171858011389071228250905826817436220577475921417653715687725614904582904992461028630081535583308130101987675856234343538955409175623400844887526162643568648833519463720377293240094456246923254350400678027273837755376406726898636241037491410966718557050759098100246789880178271925953381282421954028302759408448955014676668389697996886241636313376393903373455801407636741877711055384225739499110186468219696581651485130494222369947714763069155468217682876200362777257723781365331611196811280792669481887201298643660768551639860534602297871557517947385246369446923087894265948217008051120322365496288169035739121368338393591756418733850510970271613915439590991598154654417336311656936031122249937969999226781732358023111862644575299135758175008199839236284615249881088960232244362173771618086357015468484058622329792853875623486556440536962622018963571028812361567512543338303270029097668650568557157505516727518899194129711337690149916181315171544007728650573189557450920330185304847113818315407324053319038462084036421763703911550639789000742853672196280903477974533320468368795868580237952218629120080742819551317948157624448298518461509704888027274721574688131594750409732115080498190455803416826949787141316063210686391511681774304792596709376
>>> a = 50
>>> b = ('abacaxi')
>>> id(a)
494029216
>>> id(b)
62681120
>>> id (50)
494029216
>>> 2*a
100
>>> c = a+5
>>> c
55
>>> 
========== RESTART: C:/Users/Joao/Desktop/python/modo de edicao.py ==========
5
>>> 
========== RESTART: C:/Users/Joao/Desktop/python/modo de edicao.py ==========
25
>>> 
========== RESTART: C:/Users/Joao/Desktop/python/modo de edicao.py ==========
abacatee banana
>>> 
========== RESTART: C:/Users/Joao/Desktop/python/modo de edicao.py ==========
abacate e banana
>>> dir 'abacate'
SyntaxError: invalid syntax
>>> dir ('abacate')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help ('abacate'.upper)
Help on built-in function upper:

upper(...) method of builtins.str instance
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

>>> help (print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> a = 42
>>> b = 13
>>> a > b
True
>>> type (True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> a < b
False
>>> a == 42
True
>>> a == 52
False
>>> a != 13
True
>>> a != 52
True
>>> a
42
>>> a != 42
False
>>> nota = 7
>>> fatas = 30
>>> nota <= 6 and faltas <=20
False
>>> a
42
>>> b
13
>>> b = 42
>>> b
42
>>> a == 42 or b == 42
True
>>> a == 42 or b == 41
True
>>> a == 41 or b == 41
False
>>> c = ('alt p vai pra frente e alt n para tras')
>>> c
'alt p vai pra frente e alt n para tras'
>>> 

>>> print ('o numero eh 42')
o numero eh 42
>>> a
42
>>> b
42
>>> 
>>> print ('o numero', a , 'eh muito legal' )
o numero 42 eh muito legal
>>> print ('o numero %d eh muito legal'%a )
o numero 42 eh muito legal
>>> print ('uma fruta muito gostosa eh o %s. na minha opiniao'%a )
uma fruta muito gostosa eh o 42. na minha opiniao
>>> b = ('abacate')
>>> print ('uma fruta muito gostosa eh o %s. na minha opiniao'%b )
uma fruta muito gostosa eh o abacate. na minha opiniao
>>> uma fruta muito gostosa eh o abacate. na minha opiniao
SyntaxError: invalid syntax
>>> uma fruta muito gostosa eh o abacate. na minha opinia
SyntaxError: invalid syntax
>>> print ('uma fruta muito gostosa eh o %f. na minha opiniao'%b )
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    print ('uma fruta muito gostosa eh o %f. na minha opiniao'%b )
TypeError: must be real number, not str
>>> c = 3.141518
>>> print ('uma fruta muito gostosa eh o %f. na minha opiniao'%c )
uma fruta muito gostosa eh o 3.141518. na minha opiniao
>>> print ('uma fruta muito gostosa eh o %.2f. na minha opiniao'%c )
uma fruta muito gostosa eh o 3.14. na minha opiniao
>>> 

>>> a = 42
>>> a = ('mamao')
>>> a + ('mamao')
'mamaomamao'
>>> a + 'mamao'
'mamaomamao'
>>> a = 42
>>> b = ("mamao")
>>> a + b
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a + b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str(42) + 'mamao'
'42mamao'
>>> str(42) + ' + mamao'
'42 + mamao'
>>> '42 + mamao'
'42 + mamao'
>>> a = 42
>>> b = 13
>>> a, b = b, a
>>> a
13
>>> b
42
>>> a, b, c = 1,2,3
>>> a
1
>>> b
2
>>> c
3
>>> a, b, c, d = 'joao'
>>> a
'j'
>>> b
'o'
>>> c
'a'
>>> d
'o'
>>> divida = 0
>>> compra = 42
>>> divida = divida + compra
>>> compra = 13
>>> divida = divida + compra
>>> compra = 50
>>> divida = divida + compra
>>> print (divida)
105
>>> #www.pythontutor.com
>>> 
