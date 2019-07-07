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
  br i1 %".3", label %"iftrue143", label %"iffalse143"
exit:
iftrue143:
  store i32 1, i32* %"fat"
  br label %"repita115"
iffalse143:
  ret i32 0
ifend143:
repita115:
  %".7" = load i32, i32* %"fat"
  %".8" = load i32, i32* @"n"
  %".9" = mul i32 %".7", %".8"
  store i32 %".9", i32* %"fat"
  %".11" = load i32, i32* @"n"
  %".12" = add i32 %".11", 1
  store i32 %".12", i32* @"n"
  %".14" = load i32, i32* @"n"
  %".15" = icmp eq i32 %".14", 0
  br i1 %".15", label %"repita115", label %"repita115end"
repita115end:
  %".17" = load i32, i32* %"fat"
  ret i32 %".17"
}

define i32 @"principal"() 
{
entry:
  ret i32 0
exit:
}
