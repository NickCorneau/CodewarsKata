def loop_size(node):
  tortoise = node
  hare = node.next

  while(tortoise != hare):
    tortoise = tortoise.next
    hare = hare.next.next

  count = 1
  tortoise = tortoise.next
  
  while(tortoise != hare):
    tortoise = tortoise.next
    count = count + 1

  return count
