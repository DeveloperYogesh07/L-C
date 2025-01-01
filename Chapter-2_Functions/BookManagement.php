// Does this Book class follow SRP? 



class Book {
 
    function getTitle() {
        return "A Great Book";
    }
 
    function getAuthor() {
        return "John Doe";
    }
 
    function turnPage() {
        // pointer to next page
    }
 
    function getCurrentPage() {
        return "current page content";
    }
 
    function getLocation() {
        // returns the position in the library
        // ie. shelf number & room number
    }

    function save() {
        $filename = '/documents/'. $this->getTitle(). ' - ' . $this->getAuthor();
        file_put_contents($filename, serialize($this));
    }
}

interface Printer {
 
    function printPage($page);
}
 
class PlainTextPrinter implements Printer {
 
    function printPage($page) {
        echo $page;
    }
 
}
 
class HtmlPrinter implements Printer {
 
    function printPage($page) {
        echo '<div style="single-page">' . $page . '</div>';
    }
}


<!-- 
Responsibility 1: Represent the data and functionality of a book (e.g., getTitle, getAuthor, turnPage, getCurrentPage).
This is the primary responsibility of the Book class.

Responsibility 2: Manage library-related data (getLocation).
This introduces an unrelated responsibility of tracking physical library locations, which should be handled by another class (e.g., a Library or Location class).

Responsibility 3: Handle persistence (save).
This introduces the responsibility of saving the book's data to a file, which is unrelated to the core functionality of a Book object. File persistence should be handled by a separate service (e.g., BookRepository or BookStorage).

Thus, the Book class violates SRP because it has multiple reasons to change.
 -->