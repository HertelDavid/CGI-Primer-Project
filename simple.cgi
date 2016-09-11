#!/usr/bin/perl

use CGI;
use LWP 5.64;

require HTTP::Headers;

$query = new CGI;

print $query->header();

my $userAgent = LWP::UserAgent->new;
my $url = "http://www.facebook.com";

my $response = $userAgent->get($url);
die "Failed to retrieve $url --", $response->status_line unless $response->is_success;

my $head = $response->headers;
my $headerFields = $head->header_field_names;

for my $header ($head->header_field_names){
	print $header, ": ", $response->header($header);
	pbl();
}

sub pbl{

	print "<br/>";	

}