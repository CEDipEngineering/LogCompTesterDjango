  ADD EDX, '0'
  PUSH EDX
  INC ESI ; contador de digitos
  CMP EAX, 0
  JZ print_next ; quando acabar pula
  JMP print_dec

print_next:
  CMP ESI, 0
  JZ print_exit ; quando acabar de imprimir
  DEC ESI

  MOV EAX, SYS_WRITE
  MOV EBX, STDOUT

  POP ECX
  MOV [res], ECX
  MOV ECX, res

  MOV EDX, 1
  INT 0x80
  JMP print_next

print_exit:
  POP EBP
  RET

; subrotinas if/while
binop_je:
  JE binop_true
  JMP binop_false

binop_jg:
  JG binop_true
  JMP binop_false

binop_jl:
  JL binop_true
  JMP binop_false

binop_false:
  MOV EBX, False
  JMP binop_exit
binop_true:
  MOV EBX, True
binop_exit:
  RET

_start:

  PUSH EBP ; guarda o base pointer
  MOV EBP, ESP ; estabelece um novo base pointer

  ; codigo gerado pelo compilador
PUSH DWORD 0
MOV [EBP-4], EBX
MOV EBX, 3
PUSH EBX
MOV EBX, 1
POP EAX
ADD EAX, EBX
MOV EBX, EAX
IF_15:
MOV EBX, [EBP-4]
PUSH EBX
MOV EBX, 1
POP EAX
CMP EAX, EBX
CALL binop_jg
CMP EBX, False
JE ELSE_15
MOV [EBP-4], EBX
MOV EBX, 5
PUSH EBX
MOV EBX, 1
POP EAX
SUB EAX, EBX
MOV EBX, EAX
JMP END_IF_15
ELSE_15:
END_IF_15:
IF_23:
MOV EBX, [EBP-4]
PUSH EBX
MOV EBX, 3
POP EAX
CMP EAX, EBX
CALL binop_je
CMP EBX, False
JE ELSE_23
JMP END_IF_23
ELSE_23:
MOV [EBP-4], EBX
MOV EBX, 3
END_IF_23:
LOOP_32:
MOV EBX, [EBP-4]
PUSH EBX
MOV EBX, 5
POP EAX
CMP EAX, EBX
CALL binop_jl
CMP EBX, False
JE EXIT_32
MOV [EBP-4], EBX
MOV EBX, [EBP-4]
PUSH EBX
MOV EBX, 1
POP EAX
ADD EAX, EBX
MOV EBX, EAX
JMP LOOP_32
EXIT_32:
MOV EBX, [EBP-4]
PUSH EBX
CALL print
POP EBX
; interrupcao de saida
POP EBP
MOV EAX, 1
INT 0x80