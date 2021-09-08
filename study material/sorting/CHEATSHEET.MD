Colons can be used to align columns.

| Sorting Algorithm name        | Time Complexity           | Space Complexity    |    Stability?           | Sorting Class Type        |
| ----------------------------- |:-------------------------:|:-------------------:|:-----------------------:|--------------------------:|
| Sorting Algorithm name        | Best Case | Avg Case | worst case | worst case  |
| ----------------------------- |:-------------------------:|:-------------------:|:-----------------------:|--------------------------:|
| col 3 is      | right-aligned | $1600 |               | Tables        | Are           | Cool  |
| col 2 is      | centered      |   $12 |               | Tables        | Are           | Cool  |
| zebra stripes | are neat      |    $1 |               | Tables        | Are           | Cool  |
| Tables        | Are           | Cool  |               | Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|               | Tables        | Are           | Cool  |
| col 3 is      | right-aligned | $1600 |               | Tables        | Are           | Cool  |
| col 2 is      | centered      |   $12 |               | Tables        | Are           | Cool  |
| zebra stripes | are neat      |    $1 |               | Tables        | Are           | Cool  |
There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3


<table>
    <thead>
        <tr>
            <th>Sorting Algorithm name  </th>
            <th colspan=3>Time Complexity</th>
            <th>Space Complexity</th>
            <th>Stability?</th>
            <th>Sorting Class Type</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td></td>
            <td>Best Case</td>
            <td>Average Case</td>
            <td>Worst Case</td>
            <td>Worst Case</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Bubble Sort</td>
            <td>O(n)</td>
            <td>O(n^2)</td>
            <td>O(n^2)</td>
            <td>O(1)</td>
            <td>Yes</td>
            <td>Comparison</td>
        </tr>
        <tr>
            <td>Insertion Sort</td>
            <td>O(n)</td>
            <td>O(n^2)</td>
            <td>O(n^2)</td>
            <td>O(1)</td>
            <td>Yes</td>
            <td>Comparison</td>
        </tr>
        <tr>
            <td>Selection Sort</td>
            <td>O(n^2)</td>
            <td>O(n^2)</td>
            <td>O(n^2)</td>
            <td>O(1)</td>
            <td>Yes</td>
            <td>Comparison</td>
        </tr>
        <tr>
            <td>Merge Sort</td>
            <td>O(nlogn)</td>
            <td>O(nlogn)</td>
            <td>O(nlogn)</td>
            <td>O(n)</td>
            <td>Yes</td>
            <td>Comparison</td>
        </tr>
        <tr>
            <td>Heap Sort</td>
            <td>O(nlogn)</td>
            <td>O(nlogn)</td>
            <td>O(nlogn)</td>
            <td>O(1)</td>
            <td>No</td>
            <td>Comparison</td>
        </tr>
        <tr>
            <td>Quick Sort</td>
            <td>O(nlogn)</td>
            <td>O(nlogn)</td>
            <td>O(n^2)</td>
            <td>O(logn)</td>
            <td>No</td>
            <td>Comparison</td>
        </tr>
        <tr>
            <td>Tree Sort</td>
            <td>O(nlogn)</td>
            <td>O(nlogn)</td>
            <td>O(n^2)</td>
            <td>O(n)</td>
            <td>Yes</td>
            <td>Comparison</td>
        </tr>
        <tr>
            <td>Counting Sort</td>
            <td>O(n + k)</td>
            <td>O(n + k)</td>
            <td>O(n + k)</td>
            <td>O(k)</td>
            <td>Yes</td>
            <td>Linear</td>
        </tr>
        <tr>
            <td>Bucket Sort</td>
            <td>O(n + k)</td>
            <td>O(n + k)</td>
            <td>O(n^2)</td>
            <td>O(n)</td>
            <td>Yes</td>
            <td>Linear</td>
        </tr>
        <tr>
            <td>Radix Sort</td>
            <td>O(dn)</td>
            <td>O(dn)</td>
            <td>O(dn)</td>
            <td>O(d + n)</td>
            <td>Yes</td>
            <td>Linear</td>
        </tr>
    </tbody>
</table>