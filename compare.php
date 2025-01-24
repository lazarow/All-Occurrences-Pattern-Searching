<?php

// Get input files from command line arguments
$file1 = $argv[1];
$file2 = $argv[2];

// Read files into arrays
$lines1 = file($file1, FILE_IGNORE_NEW_LINES);
$lines2 = file($file2, FILE_IGNORE_NEW_LINES);

// Find lines in file1 that are missing from file2
$missing_from_2 = array_diff($lines1, $lines2);

// Find lines in file2 that are missing from file1 
$missing_from_1 = array_diff($lines2, $lines1);

// Output results
if (! empty($missing_from_2)) {
    echo "Lines in $file1 that are missing from $file2:\n";
    foreach ($missing_from_2 as $line) {
        echo $line . "\n";
    }
    echo "\n";
}

if (! empty($missing_from_1)) {
    echo "Lines in $file2 that are missing from $file1:\n"; 
    foreach ($missing_from_1 as $line) {
        echo $line . "\n";
    }
}

if (empty($missing_from_1) && empty($missing_from_2)) {
    echo "No differences found between $file1 and $file2\n";
}

