; ModuleID = "modulo.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

@"n" = common global i32 0, align 4
define i32 @"fatorial"(i32 %".1") 
{
entry:
  %"fat" = alloca i32, align 4
  %"v1_cmp" = load i32, i32* @"n", align 4
  %".3" = icmp sgt i32 %"v1_cmp", 0
  br i1 %".3", label %"iftrue178", label %"iffalse178"
exit:
iftrue178:
  %".5" = load i32, i32* %"fat"
  %".6" = add i32 %".5", 1
  %".7" = add i32 %".6", 3
  %".8" = load i32, i32* @"n"
  %".9" = add i32 %".8", 2
  %".10" = mul i32 %".7", %".9"
  %".11" = load i32, i32* @"n"
  %".12" = add i32 %".11", 1
iffalse178:
ifend178:
}

define i32 @"principal"() 
{
entry:
exit:
}
