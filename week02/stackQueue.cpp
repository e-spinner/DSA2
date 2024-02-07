#include <iostream>
#include <string>

// Implementation of queue using two stacks
class Queue {

private:
    // Implementation of stack using a singly linked list
    struct Stack {

    private:
        /**
         * @brief Node struct containing an integer value and a Node* link
        */
        struct Node{
        
        public:
            /**
             * @brief Node Constructor - stores input data in node and initializes Node link to NULL
             * 
             * @param newInt Input integer data to be stored in the node
            */
            Node( int newInt ) { 
                this->data = newInt;
                this-> link = NULL;
            }

            int data;
            Node* link;
        };

        // Node* to the top element of the stack
        Node* top;
        int count;

    public:
        /**
         * @brief Stack Constructor - initializes top ptr to NULL
        */
        Stack() { 
            top = NULL; 
            count = 0;
            }

        /**
         * @brief Check if stack is empty
         * 
         * @return true if empty false otherwise
        */
        bool isEmpty( void ) { return ( top == NULL ); }

        /**
         * @brief Adds a new element to the top of the stack, creates a newNode and sets it to the top
         * 
         * @param newInt Input integer sata to be stored in the newNode
        */
        void push( int newInt ) {
            // initialize newNode and link to top Node
            Node* newNode = new Node( newInt );
            newNode->link = top;
            // set newNode to be the top
            top = newNode;
            count++;
        }
        
        /**
         * @brief Removes and the topNode of the stack, checking if the stack is empty first
         * 
         * @return An integer value that was stored in the top node
        */
        int pop( void ) {
            // initialize temp to catch current top and check for empty case
            Node* temp = top;
            if ( isEmpty() ) return -1;
            else {
                // assign top to next node
                top = top->link;
                // store data, free memory, and return data
                int data = temp->data;
                delete temp;
                count--;
                return data;
            }
            return -1;
        }

        void display( void ) {
            Node* current = top;
            while( current != NULL ) {
                std::cout << current->data;
                if ( current->link != NULL ) std::cout << ", ";
                current = current->link;
            }
        }

        void reverseDisplay( void ) {
            for ( int i = count; i > 0; i-- ) {
                Node* current = top;
                for ( int j = 0; j < i-1; j++ ) current = current->link;
                std::cout << current->data;
                if ( i > 1 ) std::cout <<", ";
            }
        }
    };

    Stack enter;
    Stack exit;

public:
    Queue() {}

    /**
     * @brief pushes newInt to enter stack
     * 
     * @param newInt an integer value to be stored
    */
    void enqueue( int newInt ) {
        enter.push( newInt );
    }

    /**
     * @brief if exit stack is empty pop all from enter to exit and pop from exit to return data
     * 
     * @return integer data stored in the stack
    */
    int dequeue ( void ) {
        // check if exit stack is empty, if so flip all from enter to exit
        if ( exit.isEmpty() ) {
            while ( !enter.isEmpty() ) {
                exit.push( enter.pop() );
            }
        }
        // return top of exit stack
        return exit.pop();
    }

    void display( void ) {
        std::cout << "\nQueue: [";
        enter.display();
        if ( !exit.isEmpty() && !enter.isEmpty() ) std::cout << ", ";
        exit.reverseDisplay();
        std::cout << "]\nEnter: [";
        enter.display();
        std::cout << "] Exit: [";
        exit.display();
        std::cout << "]";
    }

};

int main ( void ) {
    Queue reginald;

    reginald.display();

    std::cout << "\n\nEnQueue 1";
    reginald.enqueue( 1 );
    std::cout << "\n\nEnQueue 2";
    reginald.enqueue( 2 );
    std::cout << "\n\nEnQueue 3\n";
    reginald.enqueue( 3 );

    reginald.display();

    std::cout << "\n\nDeQueue " << reginald.dequeue() << "\n";

    reginald.display();

    std::cout << "\n\nEnQueue 4";
    reginald.enqueue( 4 );
    std::cout << "\n\nEnQueue 5\n";
    reginald.enqueue( 5 );

    reginald.display();
    
    std::cout << "\n\nDeQueue " << reginald.dequeue();
    std::cout << "\n\nDeQueue "<< reginald.dequeue();
    std::cout << "\n\nEnQueue 6";
    reginald.enqueue( 6 );
    std::cout << "\n\nDeQueue " << reginald.dequeue();
    std::cout << "\n\nEnQueue 7\n";
    reginald.enqueue( 7 );

    reginald.display();

    std::cout << "\n\n";
}