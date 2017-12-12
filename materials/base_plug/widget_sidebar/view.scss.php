<?php
?>
.sidebar {
  height:100%;
  width:200px;
  background-color:#fff;
  position:fixed;
  z-index:1;
  overflow:auto
}

.animate-left {
  position:absolute;
  animation:animateleft 1.0s
}@keyframes animateleft{
  from{left:-300px;opacity:0} to{left:0;opacity:1}
}

@media (max-width:600px) {
  .sidebar{
    display:none;
  }
}

.sidebar-item {
  display:block;
  padding:8px;
  text-align:left;
  border:none;
  outline:none;
  white-space:normal;
  float:none;
  width:auto;
}

.sidebar-item-button {
}
