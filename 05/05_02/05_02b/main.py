from collections import deque

printer_queue = deque()
printer_queue.append("TylorSwiftTickets.pdf")
printer_queue.append("MarketingNotes.docx")
printer_queue.append("Proof.png")

while len(printer_queue) > 0:
    # popleft() method to remove an item from the front of the queue.
    document = printer_queue.popleft()
    print(f"Printing {document}")
