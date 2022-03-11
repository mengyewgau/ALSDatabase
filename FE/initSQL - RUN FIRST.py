import backendSQL as sqlFuncs

############################################
## All Member Init
############################################
id1 = "A101A"
n1 = "Hermione Granger"
f1 = "Science"
p1 = "33336663"
e1 = "flying@als.edu"
sqlFuncs.createMember(id1, n1, f1, p1, e1)

id2 = "A201B"
n2 = "Sherlock Holmes"
f2 = "Law"
p2 = "44327676"
e2 = "elementarydrw@als.edu"
sqlFuncs.createMember(id2, n2, f2, p2, e2)

id3 = "A301C"
n3 = "Tintin"
f3 = "Engineering"
p3 = "14358788"
e3 = "luvmilu@als.edu"
sqlFuncs.createMember(id3, n3, f3, p3, e3)

id4 = "A401D"
n4 = "Prinche Hamlet"
f4 = "FASS"
p4 = "16091609"
e4 = "tobeornot@als.edu"
sqlFuncs.createMember(id4, n4, f4, p4, e4)
             
id5 = "A5101E"
n5 = "Willy Wonka"
f5 = "FASS"
p5 = "19701970"
e5 = "choco1@als.edu"
sqlFuncs.createMember(id5, n5, f5, p5, e5)
           
id6 = "A601F"
n6 = "Holly Golightly"
f6 = "Business"
p6 = "55548008"
e6 = "diamond@als.edu"
sqlFuncs.createMember(id6, n6, f6, p6, e6)

id7 = "A701G"
n7 = "Raskolnikov"
f7 = "Law"
p7 = "18661866"
e7 = "oneaxe@als.edu"
sqlFuncs.createMember(id7, n7, f7, p7, e7)

id8 = "A801H"
n8 = "Patrick Bateman"
f8 = "Business"
p8 = "38548544"
e8 = "mice@als.edu"
sqlFuncs.createMember(id8, n8, f8, p8, e8)

id9 = "A901I"
n9 = "Captain Ahab"
f9 = "Science"
p9 = "18511851"
e9 = "wwhale@als.edu"
sqlFuncs.createMember(id9, n9, f9, p9, e9)

############################################
## All Book Init
############################################
an1 = "A01"
t1 = "A 1984 Story"
au1a = "George Orwell"
i1 = "9790000000001"
pub1 = "Intra S.r.l.s."
py1 = "2021"
sqlFuncs.createBook(an1, t1, i1, pub1, py1)
sqlFuncs.createBkAuthor(an1, au1a)

an2 = "A02"
t2 = "100 anos de soledad"
au2a = "Gabriel Garcia Marquez"
i2 = "9790000000002"
pub2 = "Vintage Espanol"
py2 = "2017"
sqlFuncs.createBook(an2, t2, i2, pub2, py2)
sqlFuncs.createBkAuthor(an2, au2a)

an3 = "A03"
t3 = "Brave New World"
au3a = "Aldous Huxley"
i3 = "9790000000003"
pub3 = "Harper Perennial"
py3 = "2006"
sqlFuncs.createBook(an3, t3, i3, pub3, py3)
sqlFuncs.createBkAuthor(an3, au3a)

an4 = "A04"
t4 = "Crime and Punishment"
au4a = "Fyodor Dostoevsky"
i4 = "9790000000004"
pub4 = "Penguin"
py4 = "2002"
sqlFuncs.createBook(an4, t4, i4, pub4, py4)
sqlFuncs.createBkAuthor(an4, au4a)

an5 = "A05"
t5 = "The Lion, The Witch and The Wardrobe"
au5a = "C.S. Lewis"
i5 = "9790000000005"
pub5 = "Harper Collins"
py5 = "2002"
sqlFuncs.createBook(an5, t5, i5, pub5, py5)
sqlFuncs.createBkAuthor(an5, au5a)

an6 = "A06"
t6 = "Frankenstein"
au6a = "Mary Shelley"
i6 = "9790000000006"
pub6 = "Reader's Library Classics"
py6 = "2021"
sqlFuncs.createBook(an6, t6, i6, pub6, py6)
sqlFuncs.createBkAuthor(an6, au6a)

an7 = "A07"
t7 = "The Grapes of Wrath"
au7a = "John Steinbeck"
i7 = "9790000000007"
pub7 = "Penguin Classics"
py7 = "2006"
sqlFuncs.createBook(an7, t7, i7, pub7, py7)
sqlFuncs.createBkAuthor(an7, au7a)

an8 = "A08"
t8 = "The Adventures of Huckleberry Finn"
au8a = "Mark Twain"
i8 = "9790000000008"
pub8 = "SeaWolf Press"
py8 = "2021"
sqlFuncs.createBook(an8, t8, i8, pub8, py8)
sqlFuncs.createBkAuthor(an8, au8a)

an9 = "A09"
t9 = "Great Expectations"
au9a = "Charles Dickens"
i9 = "9790000000009"
pub9 = "Penguin Classics"
py9 = "2002"
sqlFuncs.createBook(an9, t9, i9, pub9, py9)
sqlFuncs.createBkAuthor(an9, au9a)
 
an10 = "A10"
t10 = "Catch-22"
au10a = "Joseph Heller"
i10 = "9790000000010"
pub10 = "Simon & Schuster"
py10 = "2011"
sqlFuncs.createBook(an10, t10, i10, pub10, py10)
sqlFuncs.createBkAuthor(an10, au10a)

#
an11 = "A11"
t11 = "The Iliad"
au11a = "Homer"
i11 = "9790000000011"
pub11 = "Penguin Classics"
py11 = "1998"
sqlFuncs.createBook(an11, t11, i11, pub11, py11)
sqlFuncs.createBkAuthor(an11, au11a)

an12 = "A12"
t12 = "Les Miserables"
au12a = "Victor Hugo"
i12 = "9790000000012"
pub12 = "Signet"
py12 = "2013"
sqlFuncs.createBook(an12, t12, i12, pub12, py12)
sqlFuncs.createBkAuthor(an12, au12a)

an13 = "A13"
t13 = "Ulysses"
au13a = "James Joyce"
i13 = "9790000000013"
pub13 = "Vintage"
py13 = "1990"
sqlFuncs.createBook(an13, t13, i13, pub13, py13)
sqlFuncs.createBkAuthor(an13, au13a)

an14 = "A14"
t14 = "Lolita"
au14a = "Vladimir Nabokov"
i14 = "9790000000014"
pub14 = "Vintage"
py14 = "1989"
sqlFuncs.createBook(an14, t14, i14, pub14, py14)
sqlFuncs.createBkAuthor(an14, au14a)

an15 = "A15"
t15 = "Atlas Shrugged"
au15a = "Ayn Rand"
i15 = "9790000000015"
pub15 = "Dutton"
py15 = "2005"
sqlFuncs.createBook(an15, t15, i15, pub15, py15)
sqlFuncs.createBkAuthor(an15, au15a)

an16 = "A16"
t16 = "Perfume"
au16a = "Patrick Suskind"
i16 = "9790000000016"
pub16 = "Vintage"
py16 = "2001"
sqlFuncs.createBook(an16, t16, i16, pub16, py16)
sqlFuncs.createBkAuthor(an16, au16a)

an17 = "A17"
t17 = "The Metamorphosis"
au17a = "Franz Kafka"
i17 = "9790000000017"
pub17 = "12th Media Services"
py17 = "2017"
sqlFuncs.createBook(an17, t17, i17, pub17, py17)
sqlFuncs.createBkAuthor(an17, au17a)

an18 = "A18"
t18 = "American Psycho"
au18a = "Bret Easton Ellis"
i18 = "9790000000018"
pub18 = "ROBERT LAFFONT"
py18 = "2019"  
sqlFuncs.createBook(an18, t18, i18, pub18, py18)
sqlFuncs.createBkAuthor(an18, au18a)

an19 = "A19"
t19 = "Asterix the Gaul"
au19a = "Rene Goscinny"
au19b = "Albert Uderzo"
i19 = "9790000000019"
pub19 = "Papercutz"
py19 = "2020"
sqlFuncs.createBook(an19, t19, i19, pub19, py19)
sqlFuncs.createBkAuthor(an19, au19a)
sqlFuncs.createBkAuthor(an19, au19b)

an20 = "A20"
t20 = "Fahrenheit 451"
au20a = "Ray Bradbury"
i20 = "9790000000020"
pub20 = "Simon & Schuster"
py20 = "2012"
sqlFuncs.createBook(an20, t20, i20, pub20, py20)
sqlFuncs.createBkAuthor(an20, au20a)

#
an21 = "A21"
t21 = "Foundation"
au21a = "Isaac Asimov"
i21 = "9790000000021"
pub21 = "Bantam Spectra Books"
py21 = "1991"
sqlFuncs.createBook(an21, t21, i21, pub21, py21)
sqlFuncs.createBkAuthor(an21, au21a)

an22 = "A22"
t22 = "The Communist Manifesto"
au22a = "Karl Marx"
au22b = "Friedrich Engels"
i22 = "9790000000022"
pub22 = "Penguin Classics"
py22 = "2002"
sqlFuncs.createBook(an22, t22, i22, pub22, py22)
sqlFuncs.createBkAuthor(an22, au22a)
sqlFuncs.createBkAuthor(an22, au22b)

an23 = "A23"
t23 = "Rights of Man, Common Sense, and Other Political Writings"
au23a = "Thomas Paine"
i23 = "9790000000023"
pub23 = "Oxford University Press"
py23 = "2009"
sqlFuncs.createBook(an23, t23, i23, pub23, py23)
sqlFuncs.createBkAuthor(an23, au23a)

an24 = "A24"
t24 = "The Prince"
au24a = "Niccolo Machiavelli"
i24 = "9790000000024"
pub24 = "Independently published"
py24 = "2019"
sqlFuncs.createBook(an24, t24, i24, pub24, py24)
sqlFuncs.createBkAuthor(an24, au24a)

an25 = "A25"
t25 = "The Wealth of Nations"
au25a = "Adam Smith"
i25 = "9790000000025"
pub25 = "Royal Classics"
py25 = "2021"               
sqlFuncs.createBook(an25, t25, i25, pub25, py25)
sqlFuncs.createBkAuthor(an25, au25a) 

an26 = "A26"
t26 = "Don Quijote"
au26a = "Miguel de Cervantes Saavedra"
i26 = "9790000000026"
pub26 = "Ecco"
py26 = "2005"
sqlFuncs.createBook(an26, t26, i26, pub26, py26)
sqlFuncs.createBkAuthor(an26, au26a)

an27 = "A27"
t27 = "The Second Sex"
au27a = "Simone de Beauvoir"
i27 = "9790000000027"
pub27 = "Vintage"
py27 = "2011"
sqlFuncs.createBook(an27, t27, i27, pub27, py27)
sqlFuncs.createBkAuthor(an27, au27a)

an28 = "A28"
t28 = "Critique of Pure Reason"
au28a = "Immanuel Kant"
i28 = "9790000000028"
pub28 = "Cambridge University Press"
py28 = "1999"
sqlFuncs.createBook(an28, t28, i28, pub28, py28)
sqlFuncs.createBkAuthor(an28, au28a)

an29 = "A29"
t29 = "On The Origin of Species"
au29a = "Charles Darwin"
i29 = "9790000000029"
pub29 = "Signet"
py29 = "2003"
sqlFuncs.createBook(an29, t29, i29, pub29, py29)
sqlFuncs.createBkAuthor(an29, au29a)

an30 = "A30"
t30 = "Philosophae Naturalis Principia Mathematica"
au30a = "Isaac Newton"
i30 = "9790000000030"
pub30 = "University of California Press"
py30 = "2016"
sqlFuncs.createBook(an30, t30, i30, pub30, py30)
sqlFuncs.createBkAuthor(an30, au30a)

#
an31 = "A31"
t31 = "The Unbearable Lightness of Being"
au31a = "Milan Kundera"
i31 = "9790000000031"
pub31 = "Harper Perennial Modern Classics"
py31 = "2009"
sqlFuncs.createBook(an31, t31, i31, pub31, py31)
sqlFuncs.createBkAuthor(an31, au31a)

an32 = "A32"
t32 = "The Art of War"
au32a = "Sun Tzu"
i32 = "9790000000032"
pub32 = "LSC Communications"
py32 = "2007"
sqlFuncs.createBook(an32, t32, i32, pub32, py32)
sqlFuncs.createBkAuthor(an32, au32a)

an33 = "A33"
t33 = "Ficciones"
au33a = "Jorge Luis Borges"
i33 = "9790000000033"
pub33 = "Penguin Books"
py33 = "1999"
sqlFuncs.createBook(an33, t33, i33, pub33, py33)
sqlFuncs.createBkAuthor(an33, au33a)

an34 = "A34"
t34 = "El Amor en Los Tiempos del Colera"
au34a = "Gabriel Garcia Marquez"
i34 = "9790000000034"
pub34 = "Vintage"
py34 = "2007"
sqlFuncs.createBook(an34, t34, i34, pub34, py34)
sqlFuncs.createBkAuthor(an34, au34a)

an35 = "A35"
t35 = "Pedro Paramo"
au35a = "Juan Rulfo"
i35 = "9790000000035"
pub35 = "Grove Press"
py35 = "1994"
sqlFuncs.createBook(an35, t35, i35, pub35, py35)
sqlFuncs.createBkAuthor(an35, au3a)

an36 = "A36"
t36 = "The Labyrinth of Solitude"
au36a = "Octavio Paz"
i36 = "9790000000036"
pub36 = "Penguin Books"
py36 = "2008"
sqlFuncs.createBook(an36, t36, i36, pub36, py36)
sqlFuncs.createBkAuthor(an36, au36a)

an37 = "A37"
t37 = "Twenty Love Poems and a Song of Despair"
au37a = "Pablo Neruda"
i37 = "9790000000037"
pub37 = "Penguin Classics"
py37 = "2006"
sqlFuncs.createBook(an37, t37, i37, pub37, py37)
sqlFuncs.createBkAuthor(an37, au37a)

an38 = "A38"
t38 = "QED: The Strange Theory of Light and Matter"
au38a = "Richard Feynman"
i38 = "9790000000038"
pub38 = "Princeton University Press"
py38 = "2014"
sqlFuncs.createBook(an38, t38, i38, pub38, py38)
sqlFuncs.createBkAuthor(an38, au38a)

an39 = "A39"
t39 = "A Brief History of Time"
au39a = "Stephen Hawking"
i39 = "9790000000039"
pub39 = "Bantam"
py39 = "1996"
sqlFuncs.createBook(an39, t39, i39, pub39, py39)
sqlFuncs.createBkAuthor(an39, au39a)

an40 = "A40"
t40 = "Cosmos"
au40a = "Carl Sagan"
i40 = "9790000000040"
pub40 = "Ballantine Books"
py40 = "2013"
sqlFuncs.createBook(an40, t40, i40, pub40, py40)
sqlFuncs.createBkAuthor(an40, au40a)

#
an41 = "A41"
t41 = "Calculus Made Easy"
au41a = "Silvanus P. Thompson"
au41b = "Martin Gardner"
i41 = "9790000000041"
pub41 = "St Martins Pr"
py41 = "1970"
sqlFuncs.createBook(an41, t41, i41, pub41, py41)
sqlFuncs.createBkAuthor(an41, au41a)
sqlFuncs.createBkAuthor(an41, au41b)

an42 = "A42"
t42 = "Notes on Thermodynamics and Statistics"
au42a = "Enrico Fermi"
i42 = "9790000000042"
pub42 = "University of Chicago Press"
py42 = "1988"
sqlFuncs.createBook(an42, t42, i42, pub42, py42)
sqlFuncs.createBkAuthor(an42, au42a)

an43 = "A43"
t43 = "The Federalist"
au43a = "Alexander Hamilton"
au43b = "James Madison"
au43c = "John Jay"
i43 = "9790000000043"
pub43 = "Coventry House Publishing"
py43 = "2015"
sqlFuncs.createBook(an43, t43, i43, pub43, py43)
sqlFuncs.createBkAuthor(an43, au43a)
sqlFuncs.createBkAuthor(an43, au43b)
sqlFuncs.createBkAuthor(an43, au43c)

an44 = "A44"
t44 = "Second Treatise of Government"
au44a = "John Lcke"
au44b = "C. B. Macpherson"
i44 = "9790000000044"
pub44 = "Hackett Publishing Company, Inc."
py44 = "1980"
sqlFuncs.createBook(an44, t44, i44, pub44, py44)
sqlFuncs.createBkAuthor(an44, au44a)
sqlFuncs.createBkAuthor(an44, au44b)

an45 = "A45"
t45 = "The Open Society and Its Enemies"
au45a = "Karl Popper"
i45 = "9790000000045"
pub45 = "Princeton University Press"
py45 = "2020"
sqlFuncs.createBook(an45, t45, i45, pub45, py45)
sqlFuncs.createBkAuthor(an45, au45a)

an46 = "A46"
t46 = "A People's History of the United States"
au46a = "Howard Zinn"
i46 = "9790000000046"
pub46 = "Harper Perennial Modern Classics"
py46 = "2015"
sqlFuncs.createBook(an46, t46, i46, pub46, py46)
sqlFuncs.createBkAuthor(an46, au46a)

an47 = "A47"
t47 = "Lord of the Flies"
au47a = "William Golding"
i47 = "9790000000047"
pub47 = "Penguin Books"
py47 = "2003"
sqlFuncs.createBook(an47, t47, i47, pub47, py47)
sqlFuncs.createBkAuthor(an47, au47a)

an48 = "A48"
t48 = "Animal farm"
au48a = "George Orwell"
i48 = "9790000000048"
pub48 = "Wisehouse Classics"
py48 = "2021"
sqlFuncs.createBook(an48, t48, i48, pub48, py48)
sqlFuncs.createBkAuthor(an48, au48a)

an49 = "A49"
t49 = "The Old Man and the Sea"
au49a = "Ernest Hemingway"
i49 = "9790000000049"
pub49 = "Scribner"
py49 = "1995"
sqlFuncs.createBook(an49, t49, i49, pub49, py49)
sqlFuncs.createBkAuthor(an49, au49a)
         
an50 = "A50"
t50 = "Romance of the Three Kingdoms"
au50a = "Luo Guanzhong"
i50 = "9790000000050"
pub50 = "Penguin Books"
py50 = "2018"
sqlFuncs.createBook(an50, t50, i50, pub50, py50)
sqlFuncs.createBkAuthor(an50, au50a)
                    





