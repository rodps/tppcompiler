; ModuleID = "code.bc"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

declare i32 @"leiaInteiro"() 

declare float @"leiaFlutuante"() 

declare void @"escrevaInteiro"(i32 %".1") 

declare void @"escrevaFlutuante"(float %".1") 

@"a" = common global i32 0, align 4
define i32 @"main"() 
{
entry:
  %"retorno" = alloca i32
  store i32 0, i32* %"retorno"
  %"ret" = alloca i32, align 4
  store i32 10, i32* @"a"
  %".4" = load i32, i32* @"a", align 4
  %".5" = icmp sgt i32 %".4", 5
  br i1 %".5", label %"iftrue119", label %"iffalse119"
exit:
  %".19" = load i32, i32* %"retorno"
  ret i32 %".19"
iftrue119:
  %".7" = load i32, i32* @"a", align 4
  %".8" = icmp slt i32 %".7", 20
  br i1 %".8", label %"iftrue100", label %"iffalse100"
iffalse119:
  store i32 0, i32* %"ret"
  br label %"ifend119"
ifend119:
  store i32 0, i32* %"retorno"
  br label %"exit"
iftrue100:
  store i32 1, i32* %"ret"
  br label %"ifend100"
iffalse100:
  store i32 2, i32* %"ret"
  br label %"ifend100"
ifend100:
  br label %"ifend119"
}
