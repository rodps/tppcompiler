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
iffalse143:
ifend143:
}

define i32 @"principal"() 
{
entry:
exit:
}
