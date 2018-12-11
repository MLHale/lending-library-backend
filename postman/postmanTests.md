# This is the official postman tests for the backend

## Testing items

### GET /api/items
Status: Success
![](images/items_get.png)


### GET /api/items/<id>
Status: Success
![](images/items_get_by_id.png)

### POST /api/items with checkout attached
Status: Success
![](images/items_post_chk.png)

### POST /api/items without checkout attached
Status: Success
![](images/items_post_no_chk.png)

### DELETE /api/items/<id>
Status: Success seen by hitting send twice
![](images/items_del_by_id.png)

### PUT /api/items/<id>
Status: Not Implemented or cannot be determined
![]()

## Testing checkouts

### GET /api/checkouts
Status: Success
![](images/checkouts_get.png)

### GET /api/checkouts/<id>
Status: Success
![](images/checkouts_get_by_id.png)

### POST /api/checkouts
Status: Success
![](images/checkouts_post.png)

### DELETE /api/checkouts/<id>
Status: Success seen by hitting send twice
![](images/checkouts_del_by_id.png)

### PUT /api/checkouts/<id>
Status: Not implemented or cannot be determined
![]()
