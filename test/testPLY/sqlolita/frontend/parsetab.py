
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftORleftANDnonassocLELEGEGTEQNEADD ALERT ALL ALTER AND ASC CHAR CREATE DELETE DESC DROP EQ EXIT FROM GE GRANT GT HELP ID INDEX INSERT INT INTO IS KEY LE LOAD LT NE NOT NULL NUMBER ON OR PASSWORD PRIMARY PRINT REVOKE SELECT SET SHOW STRING TABLE TABLES TO UPDATE USER VALUES VIEW WHERE start : command ';'  command : ddl\n                | dml\n                | utility\n                | nothing  ddl : createtable\n            | createindex\n            | droptable\n            | dropindex\n            | showtables\n            | alerttable\n            | createuser\n            | grantuser\n            | revokeuser  dml : query\n            | insert\n            | delete\n            | update  utility : exit\n                | print  showtables : SHOW TABLES  createuser : CREATE USER ID PASSWORD STRING grantuser : GRANT power_list ON non_mrelation_list TO non_mrelation_list  revokeuser : REVOKE power_list ON non_mrelation_list FROM non_mrelation_list  power_list : power_list ',' power_type\n                   | power_type   power_type : SELECT\n                    | UPDATE\n                    | INSERT\n                    | DELETE\n                    | PRINT\n                    | ALL\n     alerttable : ALERT TABLE ID ADD attrtype\n                   | ALERT TABLE ID DROP non_mrelation_list  createtable : CREATE TABLE ID '(' non_mattrtype_list ')'  createindex : CREATE INDEX ID '(' ID ')'  droptable : DROP TABLE ID  dropindex : DROP INDEX ID '(' ID ')'  print : PRINT ID  exit : EXIT  query : SELECT non_mselect_clause FROM non_mrelation_list opwhere_clause  insert : INSERT INTO ID VALUES inservalue_list  inservalue_list : '(' non_mvalue_list ')' ',' inservalue_list\n                        | '(' non_mvalue_list ')'  delete : DELETE FROM ID opwhere_clause  update : UPDATE ID SET relattr EQ relattr_or_value opwhere_clause  non_mattrtype_list : attrtype ',' non_mattrtype_list\n                           | attrtype  attrtype : ID type\n                 | ID type '(' NUMBER ')'\n                 | PRIMARY KEY '(' ID ')'  type : INT\n             | CHAR  non_mselect_clause : non_mrelattr_list\n                           | '*'  non_mrelattr_list : relattr ',' non_mrelattr_list\n                          | relattr  relattr : ID '.' ID\n                | ID  non_mrelation_list : relation ',' non_mrelation_list\n                           | relation  relation : ID  opwhere_clause : WHERE non_mcond_list\n                       | nothing  non_mcond_list : non_mcond_list AND non_mcond_list\n                       | non_mcond_list OR  non_mcond_list\n                       | '(' non_mcond_list ')'\n                       | condition  condition : relattr op relattr_or_value\n                  | relattr EQ null_value\n                  | relattr NE null_value  relattr_or_value : relattr\n                         | value  non_mvalue_list : value ',' non_mvalue_list\n                        | value\n                        | null_value ',' non_mvalue_list\n                        | null_value  value : STRING  value : NUMBER  null_value : NULL  op : LT\n           | LE\n           | GT\n           | GE\n           | EQ\n           | NE  nothing : "
    
_lr_action_items = {'EQ':([50,85,90,110,],[-59,-58,109,134,]),'SET':([58,],[73,]),';':([0,2,3,6,8,11,12,13,15,17,18,19,21,22,23,24,25,26,28,29,30,33,50,55,57,63,74,76,78,84,85,91,92,97,100,102,104,108,111,112,114,115,116,118,119,120,121,122,124,125,128,130,131,132,133,147,150,151,152,153,154,155,156,162,163,164,],[-87,-12,-14,-20,-15,51,-11,-3,-19,-16,-8,-10,-9,-40,-6,-4,-17,-13,-5,-7,-18,-2,-59,-21,-39,-37,-87,-61,-62,-87,-58,-64,-45,-33,-34,-41,-22,-42,-68,-63,-60,-23,-38,-53,-49,-52,-24,-36,-35,-80,-79,-78,-72,-87,-73,-44,-46,-70,-69,-71,-66,-65,-67,-51,-50,-43,]),'STRING':([87,107,109,134,135,136,137,138,139,140,148,149,],[104,130,130,-85,-81,-82,-83,130,-86,-84,130,130,]),'GT':([50,85,110,],[-59,-58,137,]),'LE':([50,85,110,],[-59,-58,136,]),'KEY':([98,],[117,]),'PRIMARY':([80,88,123,],[98,98,98,]),'GRANT':([0,],[4,]),'CHAR':([99,],[118,]),'DROP':([0,64,],[5,81,]),'ALERT':([0,],[7,]),'$end':([1,51,],[0,-1,]),'TABLE':([5,7,14,],[43,44,54,]),'ALL':([4,9,60,],[35,35,35,]),'SELECT':([0,4,9,60,],[10,38,38,38,]),'WHERE':([50,74,76,78,84,85,114,128,130,131,132,133,],[-59,93,-61,-62,93,-58,-60,-79,-78,-72,93,-73,]),'*':([10,],[47,]),'.':([50,],[68,]),'ADD':([64,],[80,]),'CREATE':([0,],[14,]),'OR':([50,85,111,112,125,128,130,131,133,143,151,152,153,154,155,156,],[-59,-58,-68,141,-80,-79,-78,-72,-73,141,-70,-69,-71,-66,-65,-67,]),'SHOW':([0,],[16,]),'NE':([50,85,110,],[-59,-58,139,]),'AND':([50,85,111,112,125,128,130,131,133,143,151,152,153,154,155,156,],[-59,-58,-68,142,-80,-79,-78,-72,-73,142,-70,-69,-71,142,-65,-67,]),'INTO':([20,],[56,]),'INSERT':([0,4,9,60,],[20,36,36,36,]),'PASSWORD':([70,],[87,]),'TO':([76,77,78,114,],[-61,95,-62,-60,]),'NULL':([107,134,139,148,149,],[125,125,125,125,125,]),'EXIT':([0,],[22,]),'NUMBER':([107,109,134,135,136,137,138,139,140,145,148,149,],[128,128,-85,-81,-82,-83,128,-86,-84,158,128,128,]),'ON':([34,35,36,37,38,39,40,41,45,75,],[61,-32,-29,-26,-27,-31,-28,-30,65,-25,]),'REVOKE':([0,],[9,]),'UPDATE':([0,4,9,60,],[31,40,40,40,]),'PRINT':([0,4,9,60,],[27,39,39,39,]),'INDEX':([5,14,],[42,52,]),',':([34,35,36,37,38,39,40,41,45,46,50,75,76,78,85,105,118,119,120,125,127,128,129,130,147,162,163,],[60,-32,-29,-26,-27,-31,-28,-30,60,66,-59,-25,94,-62,-58,123,-53,-49,-52,-80,148,-79,149,-78,159,-51,-50,]),'GE':([50,85,110,],[-59,-58,140,]),'INT':([99,],[120,]),'TABLES':([16,],[55,]),'FROM':([32,46,47,48,49,50,76,78,82,83,85,114,],[59,-57,-55,67,-54,-59,-61,-62,101,-56,-58,-60,]),'USER':([14,],[53,]),'LT':([50,85,110,],[-59,-58,135,]),'DELETE':([0,4,9,60,],[32,41,41,41,]),'VALUES':([72,],[89,]),')':([50,85,96,103,105,106,111,118,119,120,125,126,127,128,129,130,131,133,143,146,151,152,153,154,155,156,157,158,160,161,162,163,],[-59,-58,116,122,-48,124,-68,-53,-49,-52,-80,147,-77,-79,-75,-78,-72,-73,156,-47,-70,-69,-71,-66,-65,-67,162,163,-76,-74,-51,-50,]),'(':([62,69,71,89,93,113,117,118,119,120,141,142,159,],[79,86,88,107,113,113,144,-53,145,-52,113,113,107,]),'ID':([10,27,31,42,43,44,52,53,54,56,59,61,65,66,67,68,73,79,80,81,86,88,93,94,95,101,109,113,123,134,135,136,137,138,139,140,141,142,144,],[50,57,58,62,63,64,69,70,71,72,74,78,78,50,78,85,50,96,99,78,103,99,50,78,78,78,50,50,99,-85,-81,-82,-83,50,-86,-84,50,50,157,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'droptable':([0,],[18,]),'relattr':([10,66,73,93,109,113,138,141,142,],[46,46,90,110,131,110,131,110,110,]),'showtables':([0,],[19,]),'createuser':([0,],[2,]),'type':([99,],[119,]),'inservalue_list':([89,159,],[108,164,]),'utility':([0,],[24,]),'dropindex':([0,],[21,]),'power_type':([4,9,60,],[37,37,75,]),'revokeuser':([0,],[3,]),'non_mcond_list':([93,113,141,142,],[112,143,154,155,]),'relation':([61,65,67,81,94,95,101,],[76,76,76,76,76,76,76,]),'createtable':([0,],[23,]),'start':([0,],[1,]),'relattr_or_value':([109,138,],[132,152,]),'opwhere_clause':([74,84,132,],[92,102,150,]),'delete':([0,],[25,]),'grantuser':([0,],[26,]),'non_mrelattr_list':([10,66,],[49,83,]),'non_mattrtype_list':([88,123,],[106,146,]),'print':([0,],[6,]),'attrtype':([80,88,123,],[97,105,105,]),'query':([0,],[8,]),'nothing':([0,74,84,132,],[28,91,91,91,]),'power_list':([4,9,],[34,45,]),'createindex':([0,],[29,]),'value':([107,109,138,148,149,],[129,133,133,129,129,]),'null_value':([107,134,139,148,149,],[127,151,153,127,127,]),'non_mrelation_list':([61,65,67,81,94,95,101,],[77,82,84,100,114,115,121,]),'update':([0,],[30,]),'command':([0,],[11,]),'alerttable':([0,],[12,]),'non_mselect_clause':([10,],[48,]),'condition':([93,113,141,142,],[111,111,111,111,]),'exit':([0,],[15,]),'ddl':([0,],[33,]),'dml':([0,],[13,]),'op':([110,],[138,]),'insert':([0,],[17,]),'non_mvalue_list':([107,148,149,],[126,160,161,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> command ;','start',2,'p_start','parser.py',20),
  ('command -> ddl','command',1,'p_command','parser.py',25),
  ('command -> dml','command',1,'p_command','parser.py',26),
  ('command -> utility','command',1,'p_command','parser.py',27),
  ('command -> nothing','command',1,'p_command','parser.py',28),
  ('ddl -> createtable','ddl',1,'p_ddl','parser.py',33),
  ('ddl -> createindex','ddl',1,'p_ddl','parser.py',34),
  ('ddl -> droptable','ddl',1,'p_ddl','parser.py',35),
  ('ddl -> dropindex','ddl',1,'p_ddl','parser.py',36),
  ('ddl -> showtables','ddl',1,'p_ddl','parser.py',37),
  ('ddl -> alerttable','ddl',1,'p_ddl','parser.py',38),
  ('ddl -> createuser','ddl',1,'p_ddl','parser.py',39),
  ('ddl -> grantuser','ddl',1,'p_ddl','parser.py',40),
  ('ddl -> revokeuser','ddl',1,'p_ddl','parser.py',41),
  ('dml -> query','dml',1,'p_dml','parser.py',46),
  ('dml -> insert','dml',1,'p_dml','parser.py',47),
  ('dml -> delete','dml',1,'p_dml','parser.py',48),
  ('dml -> update','dml',1,'p_dml','parser.py',49),
  ('utility -> exit','utility',1,'p_utility','parser.py',54),
  ('utility -> print','utility',1,'p_utility','parser.py',55),
  ('showtables -> SHOW TABLES','showtables',2,'p_showtables','parser.py',60),
  ('createuser -> CREATE USER ID PASSWORD STRING','createuser',5,'p_createuser','parser.py',65),
  ('grantuser -> GRANT power_list ON non_mrelation_list TO non_mrelation_list','grantuser',6,'p_grantuser','parser.py',70),
  ('revokeuser -> REVOKE power_list ON non_mrelation_list FROM non_mrelation_list','revokeuser',6,'p_revokeuser','parser.py',75),
  ('power_list -> power_list , power_type','power_list',3,'p_power_list','parser.py',80),
  ('power_list -> power_type','power_list',1,'p_power_list','parser.py',81),
  ('power_type -> SELECT','power_type',1,'p_power_type','parser.py',89),
  ('power_type -> UPDATE','power_type',1,'p_power_type','parser.py',90),
  ('power_type -> INSERT','power_type',1,'p_power_type','parser.py',91),
  ('power_type -> DELETE','power_type',1,'p_power_type','parser.py',92),
  ('power_type -> PRINT','power_type',1,'p_power_type','parser.py',93),
  ('power_type -> ALL','power_type',1,'p_power_type','parser.py',94),
  ('alerttable -> ALERT TABLE ID ADD attrtype','alerttable',5,'p_alerttable','parser.py',100),
  ('alerttable -> ALERT TABLE ID DROP non_mrelation_list','alerttable',5,'p_alerttable','parser.py',101),
  ('createtable -> CREATE TABLE ID ( non_mattrtype_list )','createtable',6,'p_createtable','parser.py',109),
  ('createindex -> CREATE INDEX ID ( ID )','createindex',6,'p_createindex','parser.py',114),
  ('droptable -> DROP TABLE ID','droptable',3,'p_droptable','parser.py',119),
  ('dropindex -> DROP INDEX ID ( ID )','dropindex',6,'p_dropindex','parser.py',124),
  ('print -> PRINT ID','print',2,'p_print','parser.py',129),
  ('exit -> EXIT','exit',1,'p_exit','parser.py',134),
  ('query -> SELECT non_mselect_clause FROM non_mrelation_list opwhere_clause','query',5,'p_query','parser.py',139),
  ('insert -> INSERT INTO ID VALUES inservalue_list','insert',5,'p_insert','parser.py',144),
  ('inservalue_list -> ( non_mvalue_list ) , inservalue_list','inservalue_list',5,'p_inservalue_list','parser.py',149),
  ('inservalue_list -> ( non_mvalue_list )','inservalue_list',3,'p_inservalue_list','parser.py',150),
  ('delete -> DELETE FROM ID opwhere_clause','delete',4,'p_delete','parser.py',158),
  ('update -> UPDATE ID SET relattr EQ relattr_or_value opwhere_clause','update',7,'p_update','parser.py',163),
  ('non_mattrtype_list -> attrtype , non_mattrtype_list','non_mattrtype_list',3,'p_non_mattrtype_list','parser.py',168),
  ('non_mattrtype_list -> attrtype','non_mattrtype_list',1,'p_non_mattrtype_list','parser.py',169),
  ('attrtype -> ID type','attrtype',2,'p_attrtype','parser.py',177),
  ('attrtype -> ID type ( NUMBER )','attrtype',5,'p_attrtype','parser.py',178),
  ('attrtype -> PRIMARY KEY ( ID )','attrtype',5,'p_attrtype','parser.py',179),
  ('type -> INT','type',1,'p_type','parser.py',189),
  ('type -> CHAR','type',1,'p_type','parser.py',190),
  ('non_mselect_clause -> non_mrelattr_list','non_mselect_clause',1,'p_non_mselect_clause','parser.py',195),
  ('non_mselect_clause -> *','non_mselect_clause',1,'p_non_mselect_clause','parser.py',196),
  ('non_mrelattr_list -> relattr , non_mrelattr_list','non_mrelattr_list',3,'p_non_mrelattr_list','parser.py',201),
  ('non_mrelattr_list -> relattr','non_mrelattr_list',1,'p_non_mrelattr_list','parser.py',202),
  ('relattr -> ID . ID','relattr',3,'p_relattr','parser.py',210),
  ('relattr -> ID','relattr',1,'p_relattr','parser.py',211),
  ('non_mrelation_list -> relation , non_mrelation_list','non_mrelation_list',3,'p_non_mrelation_list','parser.py',219),
  ('non_mrelation_list -> relation','non_mrelation_list',1,'p_non_mrelation_list','parser.py',220),
  ('relation -> ID','relation',1,'p_relation','parser.py',228),
  ('opwhere_clause -> WHERE non_mcond_list','opwhere_clause',2,'p_opwhere_clause','parser.py',233),
  ('opwhere_clause -> nothing','opwhere_clause',1,'p_opwhere_clause','parser.py',234),
  ('non_mcond_list -> non_mcond_list AND non_mcond_list','non_mcond_list',3,'p_non_mcond_list','parser.py',240),
  ('non_mcond_list -> non_mcond_list OR non_mcond_list','non_mcond_list',3,'p_non_mcond_list','parser.py',241),
  ('non_mcond_list -> ( non_mcond_list )','non_mcond_list',3,'p_non_mcond_list','parser.py',242),
  ('non_mcond_list -> condition','non_mcond_list',1,'p_non_mcond_list','parser.py',243),
  ('condition -> relattr op relattr_or_value','condition',3,'p_condition','parser.py',253),
  ('condition -> relattr EQ null_value','condition',3,'p_condition','parser.py',254),
  ('condition -> relattr NE null_value','condition',3,'p_condition','parser.py',255),
  ('relattr_or_value -> relattr','relattr_or_value',1,'p_relattr_or_value','parser.py',260),
  ('relattr_or_value -> value','relattr_or_value',1,'p_relattr_or_value','parser.py',261),
  ('non_mvalue_list -> value , non_mvalue_list','non_mvalue_list',3,'p_non_mvalue_list','parser.py',266),
  ('non_mvalue_list -> value','non_mvalue_list',1,'p_non_mvalue_list','parser.py',267),
  ('non_mvalue_list -> null_value , non_mvalue_list','non_mvalue_list',3,'p_non_mvalue_list','parser.py',268),
  ('non_mvalue_list -> null_value','non_mvalue_list',1,'p_non_mvalue_list','parser.py',269),
  ('value -> STRING','value',1,'p_value_string','parser.py',277),
  ('value -> NUMBER','value',1,'p_value_number','parser.py',282),
  ('null_value -> NULL','null_value',1,'p_null_value','parser.py',287),
  ('op -> LT','op',1,'p_op','parser.py',292),
  ('op -> LE','op',1,'p_op','parser.py',293),
  ('op -> GT','op',1,'p_op','parser.py',294),
  ('op -> GE','op',1,'p_op','parser.py',295),
  ('op -> EQ','op',1,'p_op','parser.py',296),
  ('op -> NE','op',1,'p_op','parser.py',297),
  ('nothing -> <empty>','nothing',0,'p_nothing','parser.py',302),
]