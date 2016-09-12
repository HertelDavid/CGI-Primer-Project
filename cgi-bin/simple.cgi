#!/usr/bin/perl

use CGI;
use LWP 5.64;
use Cwd 'abs_path';

require HTTP::Headers;

$query = new CGI;

if($ENV{"QUERY_STRING"} eq "redirect"){
	
	print $query->redirect("http://google.com");
	exit;

}

print $query->header(-type=>"text/html");

my $userAgent = LWP::UserAgent->new;
my $url = "http://www.twitter.com";
my $redirect = "http://google.com";

my $response = $userAgent->get($url);
die "Failed to retrieve $url --", $response->status_line unless $response->is_success;

my $head = $response->headers;
my $headerFields = $head->header_field_names;

if($ENV{"QUERY_STRING"} eq "HTML"){
	
	print "<html><head><title>HTML</title><link href=\"https://fonts.googleapis.com/css?family=Oxygen\" rel=\"stylesheet\"><link rel=\"stylesheet\" type=\"text/css\" href=\"http://www.csun.edu/~djh73969/styles/style.css\"></head>";
	print "<body>";
	print "<p>Written using Perl</br>Location of interpreter: ", $^X, "</p>";
	htmlPath();
	htmlEnvironment();
	htmlHeader();
	print "</body>";
	print "</html>";
	
	exit;
}

pbl();
print "Written using Perl";
pbl();
print "Location of interpreter: ", $^X;
pbl();pbl();

print "-----Absolute path of Script-----";
pbl();pbl();
print abs_path($0);
pbl();pbl();

print "-----Environment Variables-----";
pbl();pbl();

foreach my $key(keys %ENV){
	print $key, ": ", $ENV{$key};
	pbl();
}

pbl();pbl();

print "-----Response Header-----";
pbl();
print $url;
pbl();pbl();

for my $header ($head->header_field_names){
	print $header, ": ", $response->header($header);
	pbl();
}

sub pbl{

	print "<br/>";

}

sub htmlPath{

	print "<div>";
	print "<h3>-----Absolute Path of Script-----</h3>";
	print "<li>", abs_path($0), "</li>";
	print "</div>";	

}

sub htmlEnvironment{

	print "<div>";
	print "<h3>-----Environment Variables-----</h3>";
	foreach my $key(keys %ENV){
		print "<li>", $key, ": ", $ENV{$key}, "</li>";
	}
	print "</div>";	

}

sub htmlHeader{
	
	print "<div>";
	print "<h3>-----Response Header-----</h3>";
	for my $header($head->header_field_names){
		print "<li>", $header, ": ", $response->header($header), "</li>";
	}

}