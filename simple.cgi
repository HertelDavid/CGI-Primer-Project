#!/usr/bin/perl

use CGI;

$query = new CGI;

print $query->header;

foreach my $key (sort(keys(%ENV))) {

	print "$key = $ENV{$key}<br>\n";

}

print end_html;