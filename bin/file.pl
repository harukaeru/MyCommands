#!/usr/bin/perl

use strict;
use warnings;

# 読み込んだファイル内容の格納

my @data;

# デリミタを絶対にありえない文字にする

$/ = 0777;

# コマンドラインの引数からファイル名を取得

my $filename = $ARGV[0];

# ファイルを開く

open(IN, "$filename");

# ファイルの内容を入れる

@data = <IN>;

# 閉じる
close(IN);

# 置換前の文字列

my $before = qq\\;

$before = quotemeta $before;

my $after = qq\\;

# 置換する

$data[0] =~ s/$before/$after/g;

# 出力
open(OUT, "> $filename");

print OUT $data[0];
close(OUT);
