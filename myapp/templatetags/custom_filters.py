from django import template

register = template.Library()

@register.filter
def chunkify(items, chunk_size):
    """Split a list into chunks of the given size."""
    chunk_size = int(chunk_size)
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]
