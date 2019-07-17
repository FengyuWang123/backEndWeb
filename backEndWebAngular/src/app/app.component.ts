import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  public nav_part: string = 'index'

  ngOnInit () {
    this.hashChangeHandler()

    //注意：这里要有bind this绑定
    window.onhashchange = this.hashChangeHandler.bind(this)
  }

  hashChangeHandler () {
    //当用户点击了锚点的时候，我们需要获取当前的锚点标识
    const hash = window.location.hash.substr(1)
    switch (hash) {
      case '/':
        this.nav_part = 'index'
        break;
      case '/index':
        this.nav_part = 'index'
        break;
      case '/elements':
        this.nav_part = 'elements'
        break;
      case '/icons':
        this.nav_part = 'icons'
        break;
      case '/charts':
        this.nav_part = 'charts'
        break;
      case '/panels':
        this.nav_part = 'panels'
        break;
      case '/notifications':
        this.nav_part = 'notifications'
        break;
      case '/page-login':
        this.nav_part = 'page-login'
        break;
      case '/page-profile':
        this.nav_part = 'page-profile'
        break;
      case '/page-lockscreen':
        this.nav_part = 'page-lockscreen'
        break;
      case '/tables':
        this.nav_part = 'tables'
        break;
      case '/typography':
        this.nav_part = 'typography'
        break;
      }
  }
}
