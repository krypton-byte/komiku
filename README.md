# Install
```bash
$ python3 -m pip install komiku
```
# Use
```python
>>> from komiku import searchManga
>>> dow=searchManga("naruto").fetch[1]
>>> down=dow.download()
>>> down.save(f"{dow.title}.pdf")

```