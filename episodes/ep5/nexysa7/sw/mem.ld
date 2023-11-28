OUTPUT_ARCH( "riscv" )

MEMORY
{
  RAM : ORIGIN = 0x00000000, LENGTH = 0x800
}

SECTIONS
{
  .text : {
    . = ALIGN(4);
    *(.text)
    *(.text.*)
    . = ALIGN(4);
  } > RAM

  .rodata : {
    . = ALIGN(4);
    *(.srodata)
    *(.srodata.*)
    *(.rodata);
    *(.rodata.*)
    . = ALIGN(4);
  } > RAM

  .data : {
    . = ALIGN(4);
    *(.sdata)
    *(.sdata.*)
    *(.data);
    *(.data.*)
    . = ALIGN(4);
  } > RAM
}
