
// Public domain, no restrictions, Ian Holyer, University of Bristol.

// This code is from here - 
// http://www.cs.bris.ac.uk/software/shed/Text.java  


import java.util.*;

/** Provide a gap buffer for storing characters.  The raw text array, its
* length, and its offsets are made accessible to users.  The offsets are gap,
* start, and stop.  Characters 0 to (gap-1) of the text are stored in array[0]
* to array[gap-1], characters gap to (length-1) are stored in array[start] to
* array[stop-1], and a sentinel end of text character is stored in array[stop]
* to simplify code by avoiding a lot of special case tests.
**/
class Text
{
    /** The character array, managed as a gap buffer. **/
    char[] array;

    /** The length of the text. **/
    int length;

    /** The start of the gap in the text. **/
    int gap;

    /** The start of the portion of the array after the gap. **/
    int start;

    /** The end of the portion of the array after the gap. **/
    int stop;

    /** The end of text character (character '\04' = CTRL/D). **/
    final char EOT = '\04';

    /** Create an empty text array. **/
    Text()
    {
        array = new char[8];
        length = 0;
        gap = 0;
        start = array.length-1;
        stop = start;
        array[stop] = EOT;
    }

    /** Move the gap to the given position in the text. **/
    void move(int p)
    {
        if (p < gap) System.arraycopy(array, p, array, start-gap+p, gap-p);
        else if (p > gap) System.arraycopy(array, start, array, gap, p-gap);
        start = start - gap + p;
        gap = p;
    }

    /** Insert the given string at position p in the text.  After the
    * insertion, the gap is immediately after the inserted text.
    **/
    void insert(int p, String s)
    {
        int n = s.length();
        move(p);
        if (n > start-gap)
        {
            char[] old = array;
            int oldsize = array.length;
            int size = oldsize + n - (start - gap);
            size += oldsize - (size % oldsize);
            array = new char[size];
            System.arraycopy(old, 0, array, 0, gap);
            int rest = oldsize - start;
            System.arraycopy(old, oldsize-rest, array, size-rest, rest);
            start += (size - oldsize);
            stop += (size - oldsize);
        }
        char[] chars = s.toCharArray();
        System.arraycopy(chars, 0, array, p, n);
        gap += n;
    }

    /** Remove the given number of character from the text, starting
    * from the given position.  After the removal, the gap is at the removal
    * point.
    **/
    void remove(int p, int n)
    {
        if (p + n <= gap) { move(p+n); gap = gap - n; }
        else if (p >= gap) { move(p); start = start + n; }
        else { start = start + p + n - gap; gap = p; }
    }

    /** Unit testing. **/
    public static void main(String[] args)
    {
        Text text = new Text();
        text.insert(0, "abcdef");
        check("Insert", text.show(), "abcdef...");
        text.move(3);
        check("Move", text.show(), "abc...def");
        text.insert(6, "ghijklmnopqrst");
        check("Expand", text.show(), "abcdefghijklmnopqrst...");
        text.move(11);
        check("Move", text.show(), "abcdefghijk...lmnopqrst");
        text.remove(3, 3);
        check("Remove Left", text.show(), "abc...ghijklmnopqrst");
        text.remove(6, 3);
        check("Remove Right", text.show(), "abcghi...mnopqrst");
        text.remove(3, 6);
        check("Remove Straddle", text.show(), "abc...pqrst");
    }

    private String show()
    {
        String s = new String(array, 0, gap);
        s += "..." + new String(array, start, stop-start);
        return s;
    }

    private static void check(String id, Object x, Object y)
    {
        if (x == null && y == null) return;
        if (x == y) return;
        if (x != null && y != null && x.equals(y)) return;
        System.out.println("Check " + id + " failed.");
        System.out.println("Result:    " + x);
        System.out.println("Expecting: " + y);
        System.exit(1);
    }
}


