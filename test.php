<?php

for ($i = 1; $i <= 48; $i++) {
    $filename = 'dataset' . str_pad($i, 2, '0', STR_PAD_LEFT) . '.txt';
    echo 'echo ===== ' . $filename . ' =====' . PHP_EOL;
    echo 'time algorithms/automaton-on-suffix-tree/STzad11/bin/Release/net8.0/STzad11 datasets/' . $filename . ' | wc -l' . PHP_EOL;
    echo 'time algorithms/improved-naive/regex-dot/bin/Release/net8.0/regex-dot datasets/' . $filename . ' 2 | wc -l' . PHP_EOL;
}