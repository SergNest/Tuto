def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, 'a+') as fh:
      fh.write(additional_info)

      fh.seek(start_pos)

      return fh.read(count_chars)
        
    
        
        
    