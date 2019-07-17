; ModuleID = "code.bc"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

declare i32 @"leiaInteiro"() 

declare float @"leiaFlutuante"() 

declare void @"escrevaInteiro"(i32 %".1") 

declare void @"escrevaFlutuante"(float %".1") 

define i32 @"main"() 
{
entry:
  %"retorno" = alloca i32
  store i32 0, i32* %"retorno"
  store i32 0, i32* %"retorno"
  br label %"exit"
exit:
  %".5" = load i32, i32* %"retorno"
  ret i32 %".5"
}
