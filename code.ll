; ModuleID = "code.bc"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

declare i32 @"leiaInteiro"() 

declare float @"leiaFlutuante"() 

declare void @"escrevaInteiro"(i32 %".1") 

declare void @"escrevaFlutuante"(float %".1") 

define i32 @"func"(i32 %".1", float %".2") 
{
entry:
  %"retorno" = alloca i32
  store i32 0, i32* %"retorno"
  %"p1" = alloca i32, align 4
  store i32 %".1", i32* %"p1"
  %"p2" = alloca float, align 4
  store float %".2", float* %"p2"
  %"r" = alloca i32, align 4
  %".7" = load i32, i32* %"r"
  store i32 %".7", i32* %"retorno"
  br label %"exit"
exit:
  %".10" = load i32, i32* %"retorno"
  ret i32 %".10"
}

define i32 @"main"() 
{
entry:
  %"retorno" = alloca i32
  store i32 0, i32* %"retorno"
  %"x" = alloca i32, align 4
  %".3" = sitofp i32 2 to float
  %".4" = call i32 @"func"(i32 1, float %".3")
  store i32 %".4", i32* %"x"
  store i32 0, i32* %"retorno"
  br label %"exit"
exit:
  %".8" = load i32, i32* %"retorno"
  ret i32 %".8"
}
